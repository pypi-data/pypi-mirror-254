from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class NDArray(_message.Message):
    __slots__ = ("shape", "data", "dtype")
    SHAPE_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    DTYPE_FIELD_NUMBER: _ClassVar[int]
    shape: _containers.RepeatedScalarFieldContainer[int]
    data: bytes
    dtype: str
    def __init__(self, shape: _Optional[_Iterable[int]] = ..., data: _Optional[bytes] = ..., dtype: _Optional[str] = ...) -> None: ...

class PredictRequest(_message.Message):
    __slots__ = ("input", "params")
    INPUT_FIELD_NUMBER: _ClassVar[int]
    PARAMS_FIELD_NUMBER: _ClassVar[int]
    input: NDArray
    params: _struct_pb2.Struct
    def __init__(self, input: _Optional[_Union[NDArray, _Mapping]] = ..., params: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...) -> None: ...

class PredictResponse(_message.Message):
    __slots__ = ("result",)
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: NDArray
    def __init__(self, result: _Optional[_Union[NDArray, _Mapping]] = ...) -> None: ...
