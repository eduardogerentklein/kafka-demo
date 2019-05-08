from kafka import KafkaConsumer
consumer = KafkaConsumer('topic')
for msg in consumer:
  print (msg)