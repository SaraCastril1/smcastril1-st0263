from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class file_request(_message.Message):
    __slots__ = ["file"]
    FILE_FIELD_NUMBER: _ClassVar[int]
    file: str
    def __init__(self, file: _Optional[str] = ...) -> None: ...

class file_response(_message.Message):
    __slots__ = ["file"]
    FILE_FIELD_NUMBER: _ClassVar[int]
    file: bool
    def __init__(self, file: bool = ...) -> None: ...
