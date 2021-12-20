from kafka import KafkaProducer
from kafka.errors import KafkaError
import logging
from time import sleep


def send_data(**kwargs):

    producer = KafkaProducer(bootstrap_servers=['kafka:9092'])

    messages = [b"Message 1", b"Message 2", b"Messag 3"]

    for msg in messages:

        logging.info(f"Going to write {msg}")

        # Asynchronous by default
        future = producer.send('my-topic-2', value=msg)

        # Block for 'synchronous' sends
        try:
            record_metadata = future.get(timeout=10)

            # Successful result returns assigned partition and offset
            print(record_metadata)
            logging.info(
                "Metadata {}".format(record_metadata)
                )
        except KafkaError:
            # Decide what to do if produce request failed...
            logging.exception("Exception occurred")
            pass

        # Successful result returns assigned partition and offset
        print (record_metadata.topic)
        print (record_metadata.partition)
        print (record_metadata.offset)

        # sleep(1)

    producer.close()

    # produce keyed messages to enable hashed partitioning
    # producer.send('my-topic-2', key=b'tl;dr', value=b'YES')
