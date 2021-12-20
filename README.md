# kafka-docker
*Setting up a simple streaming service using kafka using docker-compose*

This repo contains a very basic example to get working with kafka and docker-compose. It serves for me as a reminder
of how to set things up in a basic way.

#### Prerequisites
Make sure you have docker-compose installed.

#### Setup
The .yml file sets up a container for kafka and its dependency zookeeper. These run on the localhost and their default 
ports. The Kafka broker lives within the Kafka container. For our purposes, we need not worry about the zookeeper 
container. Then, using the python-kafka API, we set up two clients: the producer and the consumer. The producer can send/write
messages to the broker. The consumer can get/read messages from the broker. Both clients are ran locally on the host
machine.

#### Running the application
Make sure you install the requirements (which is only kafka-python). This is necessary since we run the clients locally.
Then, the servers can be launched by simply going
```
docker-compose -f simple-docker-kafka-config.yml up
```
Open a new terminal and activate the Consumer client
```
python kafka_consumer_test
```
Since the consumer will keep listening to the broker until you tell it to stop manually (ctrl+c), the terminal will be
"taken". Therefore, open a third terminal and send data to the broker by going
```
python kafka_producer_test
```
If this succeeds, it should print some metadata. If not, it will print an exception statement. The consumer terminal 
should now show the message sent.
