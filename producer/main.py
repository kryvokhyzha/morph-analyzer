from kafka import KafkaProducer
from kafka.errors import KafkaError

from time import sleep
from json import dumps


while True:
    try:
        producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                                value_serializer=lambda x: 
                                dumps(x).encode('utf-8'))

        for e in range(1000):
            data = {'number' : e}
            producer.send('sentiment-topic', value=data)
            sleep(5)
    except:
        print('Error in producer!')

    sleep(5)