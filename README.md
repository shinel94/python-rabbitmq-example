# python RabbitMQ 사용 예제

## RabbitMQ 설치

https://www.rabbitmq.com/download.html <br>
위 링크를 확인하면, 기본적으로 Docker를 활용하여 동작하게 하는 것을 권장하고 있다. <br>
Docker만 설치되어 있다면, 별도의 복잡한 작업 없이도, RabbitMQ 서비스를 동작 시킬 수 있다.
CMD에서 아래의 명령어로 rabbitmq를 위한 docker pod를 실행 시킬 수 있다. <br>
<code>docker run -d -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 -e RABBITMQ_DEFAULT_USER=user -e RABBITMQ_DEFAULT_PASS=rmq_example rabbitmq:3.9-management</code><br>
이후
http://localhost:15672
user / rmq_example 로 접속이 가능하다

## 필요 패키지

RabbitMQ 서비스와 Python이 통신하기 위해서는 pika라는 패키지를 설치하여야 한다.<br>
<code>python -m pip install pika</code>

## 예제

* [Simple PubSub](https://github.com/shinel94/python-rabbitmq-example/tree/master/simple-pub-sub)
* [Topic PubSub](https://github.com/shinel94/python-rabbitmq-example/tree/master/topic-pub-sub)
