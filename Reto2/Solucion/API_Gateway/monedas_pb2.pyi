from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class EmptyMessage(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class PingMonedasResponse(_message.Message):
    __slots__ = ["ack"]
    ACK_FIELD_NUMBER: _ClassVar[int]
    ack: str
    def __init__(self, ack: _Optional[str] = ...) -> None: ...

class Moneda_request(_message.Message):
    __slots__ = ["data", "open", "high", "low", "close", "source"]
    DATA_FIELD_NUMBER: _ClassVar[int]
    OPEN_FIELD_NUMBER: _ClassVar[int]
    HIGH_FIELD_NUMBER: _ClassVar[int]
    LOW_FIELD_NUMBER: _ClassVar[int]
    CLOSE_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    data: str
    open: str
    high: str
    low: str
    close: str
    source: str
    def __init__(self, data: _Optional[str] = ..., open: _Optional[str] = ..., high: _Optional[str] = ..., low: _Optional[str] = ..., close: _Optional[str] = ..., source: _Optional[str] = ...) -> None: ...

class Moneda_response(_message.Message):
    __slots__ = ["data"]
    DATA_FIELD_NUMBER: _ClassVar[int]
    data: str
    def __init__(self, data: _Optional[str] = ...) -> None: ...
