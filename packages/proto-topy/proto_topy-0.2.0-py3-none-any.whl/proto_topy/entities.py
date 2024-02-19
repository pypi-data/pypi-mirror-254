from google.protobuf import descriptor_pool
from google.protobuf.message import Message
from google.protobuf.message_factory import GetMessageClassesForFiles
from google.protobuf.descriptor_pb2 import FileDescriptorSet
from google.protobuf.internal.encoder import _VarintBytes
from google.protobuf.internal.decoder import _DecodeVarint32

import os
import importlib.util
import sys
import types
from shutil import which
from pathlib import Path
from tempfile import TemporaryDirectory
from subprocess import PIPE, Popen
from typing import Dict, ClassVar, Union, Generator, Tuple, BinaryIO
from logging import getLogger


logger = getLogger(Path(__file__).name)


class ProtoModule:
    name: str
    package_path: Path
    file_path: Path
    source: str
    py_source: str
    py: types.ModuleType

    def __init__(self, file_path: Path, source: str):
        self.file_path = file_path
        self.name, _, _ = self.file_path.name.partition(".proto")
        self.source = source
        self.package_path = self.file_path.parent
        self.py = None
        self.py_source = None

    def set_module(self, content: str, global_scope: dict = None):
        self.py_source = content
        spec = importlib.util.spec_from_loader(self.name, loader=None)
        compiled_content = compile(content, self.name, "exec")
        self.py = importlib.util.module_from_spec(spec)
        exec(compiled_content, self.py.__dict__)

    def compiled(self, compiler_path: Path) -> "ProtoModule":
        collection = ProtoCollection(compiler_path, self)
        collection.compile()
        return self


class NoCompiler(Exception):
    pass


class CompilationFailed(Exception):
    pass


class ProtoCollection:
    compiler_path: Path
    modules: Dict[Path, ProtoModule]
    descriptor_data: bytes
    descriptor_set: FileDescriptorSet
    messages: dict

    def __init__(self, compiler_path: Path, *protos: ProtoModule):
        self.modules = {}
        self.compiler_path = compiler_path
        self.descriptor_data = None
        self.descriptor_set = None
        self.messages = {}
        self.pool = descriptor_pool.DescriptorPool()

        if not self.compiler_path:
            if 'PROTOC' in os.environ and os.path.exists(os.environ['PROTOC']):
                self.compiler_path = Path(os.environ['PROTOC'])
            else:
                self.compiler_path or Path(which('protoc'))
        if not self.compiler_path.is_file():
            raise FileNotFoundError()

        for proto in protos or []:
            self.add_proto(proto)

    def add_proto(self, proto: ProtoModule):
        if proto.file_path in self.modules:
            raise KeyError(f"{proto.file_path} already added")
        self.modules[proto.file_path] = proto

    def compile(self, global_scope: dict = None) -> "ProtoCollection":
        with TemporaryDirectory() as dir:
            protos_target_paths = {
                Path(dir, proto.file_path): proto for proto in self.modules.values()
            }
            proto_source_files = [
                str(file_path) for file_path in protos_target_paths.keys()
            ]
            ProtoCollection.marshal(protos_target_paths)

            compile_to_py_options = [f"--proto_path={dir}", f"--python_out={dir}"]
            ProtoCollection._do_compile(
                self.compiler_path,
                compile_to_py_options,
                proto_source_files,
                raise_exception=True,
            )

            artifact_fds_path = Path(dir, "artifacts.fds")
            compile_to_py_options = [
                "--include_imports",
                f"--proto_path={dir}",
                f"--descriptor_set_out={artifact_fds_path}",
            ]
            ProtoCollection._do_compile(
                self.compiler_path,
                compile_to_py_options,
                proto_source_files,
                raise_exception=False,
            )
            with open(str(artifact_fds_path), mode="rb") as f:
                self.descriptor_data = f.read()
            self.descriptor_set = FileDescriptorSet.FromString(self.descriptor_data)
            for file_descriptor_proto in self.descriptor_set.file:
                self.pool.Add(file_descriptor_proto)
            self.messages = GetMessageClassesForFiles([fdp.name for fdp in self.descriptor_set.file], self.pool)

            self._add_init_files(dir)

            sys.path.append(dir)
            for proto in self.modules.values():
                with open(
                    Path(dir, proto.package_path, f"{proto.name}_pb2.py")
                ) as module_path:
                    proto.set_module(module_path.read(), global_scope=global_scope)
            sys.path.pop()
        return self

    def version(self) -> str:
        outs = ProtoCollection._do_compile(
            self.compiler_path,
            ["--version"],
            [],
            raise_exception=True,
        )
        if outs:
            return outs.split()[-1].decode()

    @staticmethod
    def _do_compile(
        compiler_path: Path,
        compile_to_py_options: list,
        proto_source_files: list,
        raise_exception: bool = True,
    ) -> bytes:

        compile_command = [str(compiler_path.resolve())]
        compile_command.extend(compile_to_py_options)
        compile_command.extend(proto_source_files)
        compilation = Popen(compile_command, stdout=PIPE, stderr=PIPE)
        compilation.wait()
        outs, errs = compilation.communicate()
        if raise_exception:
            ProtoCollection._raise_for_errs(errs)
        return outs

    @staticmethod
    def _raise_for_errs(errs: bytes) -> None:
        warnings = []
        errors = []
        if not errs:
            return
        for err_line in errs.decode().strip().split("\n"):
            if "warning:" in err_line and err_line.endswith(".proto is unused."):
                warnings.append(err_line)
                continue
            errors.append(err_line)

        if warnings:
            logger.warning("\n".join(warnings))
        if errors:
            raise CompilationFailed("\n".join(errors))

    def _add_init_files(self, base_dir: Path) -> None:
        for proto in self.modules.values():
            Path(base_dir, proto.package_path, "__init__.py").touch()
            for parent_path in proto.package_path.parents:
                Path(base_dir, parent_path, "__init__.py").touch()

    @staticmethod
    def marshal(protos: Dict[Path, ProtoModule]) -> None:
        for target_file_path, proto in protos.items():
            Path(target_file_path.parent).mkdir(parents=True, exist_ok=True)
            with open(str(target_file_path), "wt") as o:
                o.write(proto.source)


class DelimitedMessageFactory:
    def __init__(
        self, stream: BinaryIO, *messages: Message, message_type: ClassVar = None
    ):
        self.stream = stream
        self.message_type = message_type
        self.offset = 0
        if message_type is None:
            self.read = self.bytes_read
        else:
            self.read = self.message_read
        if messages:
            self.write(*messages)

    def read(
        self,
    ) -> Union[Generator[Tuple[int, Message], None, None], Generator[Tuple[int, bytearray], None, None]]:
        raise NotImplementedError()

    def write(self, *messages: Message):
        for message in messages:
            if self.message_type is None:
                self.message_type = type(message)
            if not isinstance(message, self.message_type):
                raise TypeError(
                    f"Inconsistent type: {message.__class__.__name__} "
                    f"<> {self.message_type.__class__.__name__}"
                )
            self.stream.write(_VarintBytes(message.ByteSize()))
            self.stream.write(message.SerializeToString())

    def bytes_read(self) -> Generator[Tuple[int, bytes], None, None]:
        """
        :return: tuple of message offset and message bytes
        """
        buf = bytearray(self.stream.read(10))
        while buf:
            msg_len, new_pos = _DecodeVarint32(buf, 0)
            self.offset += new_pos
            buf = buf[new_pos:]
            remaining_len = msg_len - len(buf)
            if remaining_len < 0:
                yield self.offset, bytes(buf[:remaining_len])
                buf = buf[remaining_len:]
                self.offset += remaining_len
            else:
                buf.extend(self.stream.read(remaining_len))
                yield self.offset, bytes(buf)
                buf = buf[msg_len:]
                self.offset += msg_len
            buf.extend(self.stream.read(10 - len(buf)))

    def message_read(
        self, message_type: ClassVar = None
    ) -> Generator[Tuple[int, Message], None, None]:
        """
        :return: tuple of message offset and decoded bytes
        """
        buf = bytearray(self.stream.read(10))
        message_type = message_type or self.message_type
        while buf:
            message = message_type()
            msg_len, new_pos = _DecodeVarint32(buf, 0)
            self.offset += new_pos
            buf = buf[new_pos:]
            remaining_len = msg_len - len(buf)
            if remaining_len < 0:
                message.ParseFromString(bytes(buf[:remaining_len]))
                buf = buf[remaining_len:]
                self.offset += remaining_len
            else:
                buf.extend(self.stream.read(remaining_len))
                message.ParseFromString(bytes(buf))
                buf = buf[msg_len:]
                self.offset += msg_len
            yield self.offset, message
            buf.extend(self.stream.read(10 - len(buf)))
