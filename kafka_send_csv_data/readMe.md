## kafka setup on docker
```
docker-compose up -d
```

#create topic and send data
docker-compose exec kafka  bash -c "sh opt/kafka/bin/kafka-console-producer.sh --broker-list localhost:9092 --topic test"

#receive data 
docker-compose exec kafka bash -c "sh opt/kafka/bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic test --from-beginning"
