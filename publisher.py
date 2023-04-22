import pika
import json
from typing import Dict

class Publisher():
    def __init__(self) -> None:
        self.__host = "localhost"
        self.__port = 5672
        self.__username = "guest"
        self.__password = "guest"
        self.__queue = "data_queue"
        self.__exchange = "data_exchange"
        self.__rooting_key = "RK"
        self.__channel = self.__create_channel()

    def __create_channel(self):
        connection_parameters = pika.ConnectionParameters(
            host=self.__host,
            port=self.__port,
            credentials=pika.PlainCredentials(username=self.__username, password=self.__password)
        )

        channel = pika.BlockingConnection(connection_parameters).channel()
        return channel

    def send_message(self, body: Dict):
        self.__channel.basic_publish(
            exchange=self.__exchange,
            routing_key=self.__rooting_key,
            body=json.dumps(body),
            properties=pika.BasicProperties(delivery_mode=2) #mode de entrega com persistência de dados
        )


rabbitmq_publisher = Publisher()
rabbitmq_publisher.send_message({"enviando": "dicionario"})


        