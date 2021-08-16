import grpc
import location_ingest_pb2, location_ingest_pb2_grpc
from google.protobuf.timestamp_pb2 import Timestamp

channel = grpc.insecure_channel("localhost:5005", options=(('grpc.enable_http_proxy', 0),))
stub = location_ingest_pb2_grpc.LocationIngestStub(channel)


from datetime import datetime

now = datetime.now()
print(now.isoformat())

timestamp = Timestamp()

location_data = location_ingest_pb2.LocationIngestMessage(
    person_id = 3,
    longitude = "123.345",
    latitude = "24.543",
    creation_time= "2021-08-09T07:00:24.019096Z"
)

response = stub.Create(location_data)