import pika
from constant import RABBIT_MQ_SERVICE_HOST, RABBIT_MQ_USER_ID, RABBIT_MQ_USER_PWD, RABBIT_MQ_TOPIC_ROUTING_KEY, RABBIT_MQ_TOPIC_EXCHANGE_NAME

if __name__ == '__main__':


    credentials = pika.PlainCredentials(RABBIT_MQ_USER_ID, RABBIT_MQ_USER_PWD)
    parameters = pika.ConnectionParameters(host=RABBIT_MQ_SERVICE_HOST,
                                           credentials=credentials)  # port 파라미터의 경우 할당하지 않으면 default인 5672가 할당
    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()

    channel.exchange_declare(exchange=RABBIT_MQ_TOPIC_EXCHANGE_NAME, exchange_type='topic')  # topic exchange를 설정하고, rabbitMQ에 등록해 둔다.

    result = channel.queue_declare('', exclusive=True)
    queue_name = result.method.queue

    channel.queue_bind(exchange=RABBIT_MQ_TOPIC_EXCHANGE_NAME, queue=queue_name, routing_key=RABBIT_MQ_TOPIC_ROUTING_KEY)
    # topic exchange를 사용할 때 routing key를 기준으로 routing key에 입력한 조건에 맞는 모든 subscriber에게 메세지가 전달된다.
    # 이때 routing_key에는 wild card ( * ) 를 사용할 수 있다.
    # example)
    # subscriber가 routing key를 '*.*' 로 subscribe를 하고 있는 경우
    # publisher의 routing key가 'major.minor' 로 publish 한 메세지와 'major.major' 로 publish 한 메세지를 모두 받을 수 있다.


    def callback(ch, method, properties, body):
        print(f" [x] Received %r" % body)

    channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True) # 동일하게 메세지를 전달 받을 때 실행하는 callback함수를 구현하고 할당하면 된다.

    print(' [*] Waiting for messages. To exit press CTRL+C')

    channel.start_consuming()

