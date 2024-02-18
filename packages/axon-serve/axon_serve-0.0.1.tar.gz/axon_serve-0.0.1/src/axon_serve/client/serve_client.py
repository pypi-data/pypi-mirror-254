import grpc
from numpy import dtype, ndarray
from typing import Any, Union

from axon_serve.convert.convert_array import deserialize_array, serialize_array
from axon_serve.convert.convert_dict import dict_to_struct
from axon_serve.proto.generated.service_pb2 import PredictRequest, PredictResponse
from axon_serve.proto.generated.service_pb2_grpc import ServeModelStub

from axon_serve.options import CHANNEL_OPTIONS


ndarray = ndarray[Any, dtype[Any]]


class ModelServeClient():
    def __init__(self, host: str, port: int):
        self.channel = grpc.insecure_channel(
            f'{host}:{port}', options=CHANNEL_OPTIONS)

        self.stub = ServeModelStub(self.channel)

    def predict(self, model_input: ndarray, params: Union[dict[str, Any], None] = None) -> ndarray:
        request = self.__prepare_request(model_input, params)

        return self.__make_call(request)

    def __make_call(self, request: PredictRequest) -> ndarray:
        response: PredictResponse = self.stub.Predict(request)
        result = deserialize_array(response.result)

        return result

    def __prepare_request(self, model_input: ndarray, params: Union[dict[str, Any], None] = None) -> PredictRequest:
        serialized_input = serialize_array(model_input)
        serialized_params = None

        if params:
            serialized_params = dict_to_struct(params)

        request = PredictRequest(
            input=serialized_input, params=serialized_params)

        return request
