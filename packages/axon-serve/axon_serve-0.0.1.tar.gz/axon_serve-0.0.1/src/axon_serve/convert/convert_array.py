from typing import Any
import numpy as np
from numpy import dtype, ndarray

from axon_serve.proto.generated.service_pb2 import NDArray


def serialize_array(array: ndarray[Any, dtype[Any]]) -> NDArray:
    shape = array.shape
    dtype = array.dtype.name
    array_bytes = array.flatten().tobytes()
    serialized_array = NDArray(data=array_bytes, dtype=dtype, shape=shape)

    return serialized_array


def deserialize_array(serialized_array: NDArray) -> ndarray[Any, dtype[Any]]:
    array = np.frombuffer(serialized_array.data, dtype=serialized_array.dtype)
    array = array.reshape(serialized_array.shape)

    return array
