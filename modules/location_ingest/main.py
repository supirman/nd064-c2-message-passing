import time
from concurrent import futures

from google.protobuf.json_format import MessageToJson, MessageToDict
from kafka import KafkaProducer
import grpc
import location_ingest_pb2
import location_ingest_pb2_grpc

TOPIC_NAME = 'udaconnect-location'
KAFKA_SERVER = 'udaconnect-kafka-0.udaconnect-kafka-headless.default.svc.cluster.local:9092'

class LocationIngestServicer(location_ingest_pb2_grpc.LocationIngestServicer):
    def Create(self, request, context):

        json_value = MessageToJson(request,preserving_proto_field_name=True)
        
        producer = KafkaProducer(bootstrap_servers=KAFKA_SERVER)

        producer.send(TOPIC_NAME, str.encode(json_value))
        producer.flush()
        print(json_value)
        return location_ingest_pb2.LocationIngestMessage(**MessageToDict(request, True, True))


# Initialize gRPC server
server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
location_ingest_pb2_grpc.add_LocationIngestServicer_to_server(LocationIngestServicer(), server)


print("Server starting on port 5005...")
server.add_insecure_port("[::]:5005")
server.start()

# Keep thread alive
try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)