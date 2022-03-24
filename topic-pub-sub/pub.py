import pika
from constant import RABBIT_MQ_SERVICE_HOST, RABBIT_MQ_USER_ID, RABBIT_MQ_USER_PWD, RABBIT_MQ_TOPIC_EXCHANGE_NAME, RABBIT_MQ_TOPIC_PUB_ROUTING_KEY_LIST

if __name__ == '__main__':
    credentials = pika.PlainCredentials(RABBIT_MQ_USER_ID, RABBIT_MQ_USER_PWD)
    parameters = pika.ConnectionParameters(host=RABBIT_MQ_SERVICE_HOST, credentials=credentials) # port 파라미터의 경우 할당하지 않으면 default인 5672가 할당
    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()

    channel.exchange_declare(exchange=RABBIT_MQ_TOPIC_EXCHANGE_NAME,
                             exchange_type='topic')  # topic exchange를 설정하고, rabbitMQ에 등록해 둔다.

    # queue name에 해당하는 루트로 publishing을 진행한다.
    # queue를 명시적으로 선언하여 RabbitMQ 서버에 추가하는 작업 같으나, 진행하지 않아도 동작은 됨

    for routing_key in RABBIT_MQ_TOPIC_PUB_ROUTING_KEY_LIST:

        channel.basic_publish(exchange='topic', routing_key=routing_key, body=b'Hello World!')
    # exchange의 경우 type별로 추가로 declare한 exchange가 있는 경우 할당하고,
    # 없으면, Direct Exchange가 할당 되는 것으로 파악,
    # routing_key는 Fanout이나 Topic Exchange가 설정된 경우에 활용된다.
    # queue 이름이나 다른 key를 할당할 수 있다. 이때 routing key를 기준으로 메세지가 전달 publishing을 진행한다.
    connection.close()