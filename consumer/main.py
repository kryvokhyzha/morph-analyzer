from kafka import KafkaConsumer
from json import loads
from time import sleep


while True:
    try:
        consumer = KafkaConsumer(
            'sentiment-topic',
            bootstrap_servers=['localhost:9092'],
            auto_offset_reset='earliest',
            enable_auto_commit=True,
            value_deserializer=lambda x: loads(x.decode('utf-8')))

        for message in consumer:
            message = message.value
            print('{} added'.format(message))
    except:
        print('Error in consumer!')
    
    sleep(5)
