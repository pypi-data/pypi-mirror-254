# AxonServe

Simple package for ML Model serving with gRPC

## Installation

```bash
$ pip install axon_serve
```

## Usage

### Server

```python
from axon_serve import PredictionService, GRPCService

# implement PredictionService class
class TestPredictionService(PredictionService):
    def __init__(self)
        super().__init__()

	# override predict method with your custom prediction logic
	# model_input and return values must be numpy arrays
	# params is a dict with optional kwargs for model
    def predict(self, model_input, params):

        print("model_input: ", model_input.shape)
        print("params: ", params)

        return model_input

if __name__ == "__main__":
	# instantiate your prediction service
	test_prediction_service = TestPredictionService()

	# register it with GRPCService providing the port
	service = GRPCService(test_prediction_service, port=5005)

	# start the server
	service.start()
```

### Client

```python
from axon_serve import ModelServeClient

# instantiate the client providing host and port
serve_client = ModelServeClient(host="localhost", port=5005)

model_input = np.array([1, 2, 3])
params = {"test_param": true}

# call predict method to send request to server
result = serve_client.predict(model_input, params)

print(result.shape)
```

## TODOs

-   [ ] add tests
-   [ ] add support for secure channels
-   [ ] add support for arbitrary tensor serialization
