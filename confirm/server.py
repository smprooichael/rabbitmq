import pika
import time

credentials = pika.PlainCredentials('Meysam', 'maisam')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', credentials=credentials))
ch = connection.channel()

ch.exchange_declare(exchange='main', exchange_type='direct', durable=True, auto_delete=False)
ch.queue_declare(queue='mainq', durable=True, auto_delete=False, exclusive=False)


def callback(ch, method, properties, body):
    print(body)

ch.basic_consume(queue='mainq', on_message_callback=callback)
print('start consuming...')
ch.start_consuming()