# Tutorial Kafka Docker

1. Baixe o Apache Kafka e descompacte em um diretório da sua máquina

```
https://www.apache.org/dyn/closer.cgi?path=/kafka/2.2.0/kafka_2.12-2.2.0.tgz
```

2. Iniciando o Zookeeper

```
cd kafka_2.12-2.2.0
Linux/Osx: bin/zookeeper-server-start.sh ../config/zookeeper.properties
Windows: bin/windows/zookeeper-server-start.bat ../config/zookeeper.properties
```

3. Iniciando o Kafka

```
Linux/Osx: bin/kafka-server-start.sh config/server.properties
Windows: bin/windows/kafka-server-start.bat config/server.properties
```

4. Criar topico

``` 
Linux/Osx: bin/kafka-topics.sh --create --topic topic --partitions 1 --zookeeper localhost:2181 --replication-factor 1
Windows: bin/windows/kafka-topics.bat --create --topic topic --partitions 1 --zookeeper localhost:2181 --replication-factor 1
```

5. Verificando se o topico foi criado com sucesso

```
Linux/Osx: bin/kafka-topics.sh --describe --topic topic --zookeeper localhost:2181
Windows: bin/windows/kafka-topics.bat --describe --topic topic --zookeeper localhost:2181
```

6. Iniciando o consumer

```
Linux/Osx: bin/kafka-console-consumer.sh --topic=topic --bootstrap-server localhost:9092
Windows: bin/windows/kafka-console-consumer.bat --topic=topic --bootstrap-server localhost:9092
```

7. Iniciando o producer

```
Linux/Osx: bin/kafka-console-producer.sh --topic=topic --broker-list localhost:9092
Windows: bin/windows/kafka-console-producer.bat --topic=topic --broker-list localhost:9092
```
