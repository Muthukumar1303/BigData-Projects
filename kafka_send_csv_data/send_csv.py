import pandas as pd
from kafka import KafkaProducer
from kafka.errors import KafkaError
import json
import time

# Read the CSV file
df = pd.read_csv('inc_dataset.csv')

# Create a Kafka producer
producer = KafkaProducer(bootstrap_servers=['localhost:9092'])

# Convert each row to a JSON object and send it to the topic
for index, row in df.iterrows():
    d = row.to_dict()
    data = json.dumps(d)
    future = producer.send('test', data.encode())
    time.sleep(5)
    try:
        record_metadata = future.get(timeout=10)
        print(record_metadata.topic)
        print(record_metadata.partition)
        print(record_metadata.offset)
    except KafkaError as e:
        # Decide what to do if produce request failed...
        e.exception()
        pass

# Close the producer
producer.close()