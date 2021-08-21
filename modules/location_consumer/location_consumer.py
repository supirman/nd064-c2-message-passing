from kafka import KafkaConsumer
import requests
import logging

logger = logging.getLogger("udaconnect-api")

TOPIC_NAME = 'udaconnect-location'
BOOTSTRAP_SERVER=["udaconnect-kafka:9092"]
LOCATION_SERVICE="http://udaconnect-location:5000"

consumer = KafkaConsumer(TOPIC_NAME, bootstrap_servers=BOOTSTRAP_SERVER, group_id=TOPIC_NAME)
for message in consumer:
    r = requests.post(LOCATION_SERVICE+"/api/locations", json=message)
    logger.info(r.json())