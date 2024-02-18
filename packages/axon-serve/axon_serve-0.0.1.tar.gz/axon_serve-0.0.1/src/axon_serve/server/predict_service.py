from abc import ABC, abstractmethod
from typing import Any, Union
import grpc
from numpy import dtype, ndarray

from axon_serve.convert.convert_dict import struct_to_dict
from axon_serve.convert.convert_array import deserialize_array, serialize_array
from axon_serve.proto.generated.service_pb2_grpc import ServeModelServicer, add_ServeModelServicer_to_server
from axon_serve.proto.generated.service_pb2 import PredictRequest, PredictResponse

ndarray = ndarray[Any, dtype[Any]]


class PredictionService(ABC, ServeModelServicer):
    def Predict(self, request: PredictRequest, context: grpc.RpcContext) -> PredictResponse:
        mode_input = deserialize_array(request.input)

        params = None
        if (request.HasField("params")):
            params = struct_to_dict(request.params)

        result = self.predict(mode_input, params)

        result_serialized = serialize_array(result)
        response = PredictResponse(result=result_serialized)

        return response

    def add_to_server(self, server: grpc.Server):
        add_ServeModelServicer_to_server(self, server)

    @abstractmethod
    def predict(self, model_input: ndarray, params: Union[dict[str, Any], None]) -> ndarray:
        pass
