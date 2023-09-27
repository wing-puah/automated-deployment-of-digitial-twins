from time import sleep
from confluent_kafka import Producer

producer = Producer({'bootstrap.servers': 'kafka:9092'})

i = 1
while True:
    producer.produce('my-topic', key='key', value=f'message {i}')
    i += 1
    producer.flush()
    sleep(10)
