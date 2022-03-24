import pika, sys, os
from constant import RABBIT_MQ_PUB_SUB_QUEUE_NAME, RABBIT_MQ_USER_PWD, RABBIT_MQ_USER_ID, RABBIT_MQ_SERVICE_HOST

def main():
    credentials = pika.PlainCredentials(RABBIT_MQ_USER_ID, RABBIT_MQ_USER_PWD)
    parameters = pika.ConnectionParameters(host=RABBIT_MQ_SERVICE_HOST,
                                           credentials=credentials)  # port 파라미터의 경우 할당하지 않으면 default인 5672가 할당
    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()

    channel.queue_declare(queue=RABBIT_MQ_PUB_SUB_QUEUE_NAME)

    def callback(ch, method, properties, body):  # RabbitMQ에서 구독중인 queue로 부터 메세지를 전달 받을 때, 실행되어질 콜백 함수
        print("Received")
        print(body)  # publisher가 보낸 body의 bytes가 보여진다.

    channel.basic_consume(queue=RABBIT_MQ_PUB_SUB_QUEUE_NAME, on_message_callback=callback, auto_ack=True)
    # queue name에 대해서 구독을 시작하고, queue name에 해당하는 queue로 값이 insert 되는 시점에서 on_message_callback이 실행된다.
    # 이때 같은 queue name으로 여러개의 subscriber가 존재한다면, direct exchange의 경우 1개의 subscriber에게만 입력한 메세지가 전달된다.

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)