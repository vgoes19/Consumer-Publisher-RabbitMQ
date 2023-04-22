import pika

class RabbiMQConsumer:
    def __init__(self, data_callback) -> None:
        self.__host = "localhost"
        self.__port = 5672
        self.__username = "guest"
        self.__password = "guest"
        self.__queue = "data_queue3"
        self.__callback = data_callback
        self.__channel = self.__create_channel()

    def __create_channel(self):
        #Onde rabbitMQ está atuando
        connection_parameteres = pika.ConnectionParameters(
            host=self.__host,
            port=self.__port,
            credentials=pika.PlainCredentials(username=self.__username, password=self.__password)
        )

        channel = pika.BlockingConnection(connection_parameteres).channel()
        channel.queue_declare(
            queue=self.__queue, 
            durable=True, 
            arguments={
                "x-overflow": "reject-publish"
            }
        )

        channel.basic_consume(
            queue=self.__queue,
            auto_ack=True,
            on_message_callback=self.__callback
        )

        return channel
    
    def start(self):
        print('Listen RabbitMQ in Port 5672')
        self.__channel.start_consuming()


def data_callback(ch, method, properties, body):
    print(body) #lendo em bytes


RabbiMQConsumer = RabbiMQConsumer(data_callback)
RabbiMQConsumer.start()