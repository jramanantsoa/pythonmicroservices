import pika

params = pika.URLParameters('amqps://bjwowohd:5YReuUJOtq0LEsRHpQMyRjjs3vwz-BQc@chinook.rmq.cloudamqp.com/bjwowohd')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='main')


def callback(ch, method, properties, body):
    print('Received in main')
    print(body)


channel.basic_consume(queue='main', on_message_callback=callback)
print('Started consuming')
channel.start_consuming()
channel.close()
