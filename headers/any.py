import pika
from pika.exchange_type import ExchangeType

credentails = pika.PlainCredentials('Meysam', 'maisam')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', credentials=credentails))
ch = connection.channel()

ch.exchange_declare(exchange='he', exchange_type=ExchangeType.headers)
ch.queue_declare(queue='hq-any', exclusive=True)

bind_args = {'x-match':'any', 'name':'Meysam', 'age':'23'}

ch.queue_bind(queue='hq-any', exchange='he', arguments=bind_args)

def callback(ch, method, properties, body):
    print(f'Received {body}')

ch.basic_consume(queue='hq-any', on_message_callback=callback, auto_ack=True)

print("Waiting...")
ch.start_consuming()