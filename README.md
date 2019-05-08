# Tutorial Kafka Docker

1. Iniciando o Zookeeper

```
Linux/Osx: bin/zookeeper-server-start.sh ../config/zookeeper.properties
Windows: bin/windows/zookeeper-server-start.bat ../config/zookeeper.properties
```

2. Iniciando o Kafka

```
Linux/Osx: bin/kafka-server-start.sh config/server.properties
Windows: bin/windows/kafka-server-start.bat config/server.properties
```

3. Criar topico

``` 
Linux/Osx: bin/kafka-topics.sh --create --topic topic --partitions 1 --zookeeper localhost:2181 --replication-factor 1
Windows: bin/windows/kafka-topics.bat --create --topic topic --partitions 1 --zookeeper localhost:2181 --replication-factor 1
```

4. Verificando se o topico foi criado com sucesso

```
Linux/Osx: bin/kafka-topics.sh --describe --topic topic --zookeeper localhost:2181
Windows: bin/windows/kafka-topics.bat --describe --topic topic --zookeeper localhost:2181
```

5. Iniciando o consumer

```
Linux/Osx: bin/kafka-console-consumer.sh --topic=topic --bootstrap-server localhost:9092
Windows: bin/windows/kafka-console-consumer.bat --topic=topic --bootstrap-server localhost:9092
```

6. Iniciando o producer

```
Linux/Osx: bin/kafka-console-producer.sh --topic=topic --broker-list localhost:9092
Windows: bin/windows/kafka-console-producer.bat --topic=topic --broker-list localhost:9092
```
