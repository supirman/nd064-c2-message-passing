import grpc
import location_ingest_pb2, location_ingest_pb2_grpc

channel = grpc.insecure_channel("localhost:30005", options=(('grpc.enable_http_proxy', 0),))
stub = location_ingest_pb2_grpc.LocationIngestStub(channel)



location_data = location_ingest_pb2.LocationIngestMessage(
    person_id = 6,
    longitude = "37.55363",
    latitude = "-122.290883",
    creation_time= "2020-07-07T10:37:06"
)

response = stub.Create(location_data)