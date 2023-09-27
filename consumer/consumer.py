from confluent_kafka import Consumer, KafkaError

consumer = Consumer({
    'bootstrap.servers': 'kafka:9092',
    'group.id': 'my-group',
    'auto.offset.reset': 'earliest'
})

consumer.subscribe(['my-topic'])

while True:
    msg = consumer.poll(1.0)

    if msg is None:
        continue
    if msg.error():
        if msg.error().code() == KafkaError._PARTITION_EOF:
            print('Reached end of partition')
        else:
            print('Error: %s' % msg.error())
    else:
        print('Received message: %s' % msg.value())
