import json
import os

from kafka import KafkaProducer
from time import sleep


FILE_NAME = 'wiki_dump.tokenized.txt'
KAFKA_BROKER_URL = os.environ.get('KAFKA_BROKER_URL')
TRANSACTIONS_TOPIC = os.environ.get('TRANSACTIONS_TOPIC')
TRANSACTIONS_PER_SECOND = float(os.environ.get('TRANSACTIONS_PER_SECOND'))
SLEEP_TIME = 1 / TRANSACTIONS_PER_SECOND


if __name__ == '__main__':
    producer = KafkaProducer(
        bootstrap_servers=KAFKA_BROKER_URL,
        # Encode all values as JSON
        value_serializer=lambda value: json.dumps(value).encode(),
    )
    with open(FILE_NAME, 'r') as file:
        for line in file:
            producer.send(TRANSACTIONS_TOPIC, value=line)
            sleep(SLEEP_TIME)
