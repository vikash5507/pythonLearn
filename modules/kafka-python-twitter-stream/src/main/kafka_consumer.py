from config import KAFKA_TOPIC, KAKFKA_BOOTSTRAP_SERVER
import json
from kafka import KafkaConsumer

def deserialize(record_val):
    return record_val.decode("utf-8")
    # return json.loads(record.value)

if __name__ == "__main__":
    
    consumer = KafkaConsumer(
        KAFKA_TOPIC, 
        bootstrap_servers=KAKFKA_BOOTSTRAP_SERVER,
        auto_offset_reset="earliest"
    )

    for record in consumer:
        print(deserialize(record.value))
