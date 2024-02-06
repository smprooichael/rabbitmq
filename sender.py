import pika
import time

credentials = pika.PlainCredentials('Meysam', 'maisam')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', credentials=credentials))
ch = connection.channel()

ch.queue_declare(queue='one')
ch.basic_publish(exchange='', routing_key='one', body='Hello world...', properties=pika.BasicProperties(
    headers={"name":"meysam", "age":"23"},
))
print('Message was sent.')
connection.close()