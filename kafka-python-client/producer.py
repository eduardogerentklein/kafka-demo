from kafka import KafkaProducer
producer = KafkaProducer(bootstrap_servers='localhost:9092')
future = producer.send('topic', b'teste')
result = future.get(timeout=60)