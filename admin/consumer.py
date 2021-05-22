import pika

params = pika.URLParameters('amqps://bjwowohd:5YReuUJOtq0LEsRHpQMyRjjs3vwz-BQc@chinook.rmq.cloudamqp.com/bjwowohd')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='admin')


def callback(ch, method, properties, body):
    print('Receive in admin')
    print(body)


channel.basic_consume(queue='admin', on_message_callback=callback)
print('Started consuming')
channel.start_consuming()
channel.close()
