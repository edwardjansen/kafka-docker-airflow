# kafka-docker
*Setting up a simple streaming service using kafka & airflow using docker-compose*

This repo contains a very basic example to get working with kafka, airflow and docker-compose. It serves for me as a 
reminder of how to set things up in a basic way.

#### Prerequisites
Make sure you have docker-compose installed.

#### Setup
The .yml file sets up a container for kafka, its dependency zookeeper, airflow and its dependency postgres. 
These connect to the localhost via their default ports. The Kafka broker lives within the Kafka container. For our purposes, 
we need not worry about the zookeeper and postgres containers. Then, using the python-kafka API, we set up two clients: 
the producer and the consumer. The producer can send/write messages to the broker. The consumer can get/read messages 
from the broker. Both clients will be triggered by an Airflow DAG and will thus run on the Airflow server. As such, the
Airflow server needs to have python-kafka installed. To achieve this, we have a separate Dockerfile in the airflow_docker
folder whose purpose it is to execute ```pip install requirements.txt``` within the container. We'll schedule the DAGs
to trigger only ``@once``, i.e. on start-up. We'll be able to manually trigger the DAGs as well via the GUI available
at the port specified in the .yml file.

#### Running the application
Since the clients run on the airflow container, there is no need to install requirements locally.
The servers can be launched by simply going
```
docker-compose -f simple-docker-kafka-config.yml up
```
(Strictly speaking, you'll first need to build the image using the same cmd but with 'up' replaced by 'build'. However,
I seem to have observed that docker compose will do this automatically if you go for 'up' right away.)

Access the Airflow GUI via ``localhost:8080`` and toggle the DAGs on. This will trigger the first run. After this,
you can trigger runs yourself using the GUI.
