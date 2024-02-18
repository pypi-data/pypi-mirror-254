import grpc
from concurrent import futures

from axon_serve.server.predict_service import PredictionService
from axon_serve.options import CHANNEL_OPTIONS


class GRPCService():
    def __init__(self, service_impl: PredictionService, port: int, max_workers: int = 10):
        self.service_impl = service_impl
        self.port = port
        self.max_workers = max_workers

    def start(self):
        server = grpc.server(
            thread_pool=futures.ThreadPoolExecutor(
                max_workers=self.max_workers),
            options=CHANNEL_OPTIONS
        )

        self.service_impl.add_to_server(server)
        server.add_insecure_port(f'[::]:{self.port}')

        print(f"Starting gRPC server on port {self.port}...")
        server.start()
        server.wait_for_termination()
