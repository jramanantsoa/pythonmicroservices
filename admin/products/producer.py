# amqps://bjwowohd:5YReuUJOtq0LEsRHpQMyRjjs3vwz-BQc@chinook.rmq.cloudamqp.com/bjwowohd
import pika

params = pika.URLParameters('amqps://bjwowohd:5YReuUJOtq0LEsRHpQMyRjjs3vwz-BQc@chinook.rmq.cloudamqp.com/bjwowohd')

connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish():
    channel.basic_publish(exchange='', routing_key='admin', body='hello')
