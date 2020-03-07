import os
import re
import json

from kafka import KafkaConsumer

import pymorphy2


KAFKA_BROKER_URL = os.environ.get('KAFKA_BROKER_URL')
TRANSACTIONS_TOPIC = os.environ.get('TRANSACTIONS_TOPIC')


if __name__ == '__main__':
    consumer = KafkaConsumer(
        TRANSACTIONS_TOPIC,
        bootstrap_servers=KAFKA_BROKER_URL,
        value_deserializer=json.loads,
    )

    morph = pymorphy2.MorphAnalyzer(lang='uk')

    for idx, message in enumerate(consumer):
        all_words = re.findall(r'\s*([\w-]+)', message.value)
        for word in all_words:
            p = morph.parse(word)[0]
            print(p.normal_form)
        
