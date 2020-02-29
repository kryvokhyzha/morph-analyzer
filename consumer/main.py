import os
import json

from kafka import KafkaConsumer


KAFKA_BROKER_URL = os.environ.get('KAFKA_BROKER_URL')
TRANSACTIONS_TOPIC = os.environ.get('TRANSACTIONS_TOPIC')


if __name__ == '__main__':
    consumer = KafkaConsumer(
        TRANSACTIONS_TOPIC,
        bootstrap_servers=KAFKA_BROKER_URL,
        value_deserializer=json.loads,
    )

    for idx, message in enumerate(consumer):
        transaction = message.value
        print(f'{idx}. Counsumer get msg:', transaction)
