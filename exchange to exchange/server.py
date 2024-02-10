import pika

credentials = pika.PlainCredentials('Meysam', 'maisam')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', credentials=credentials))
ch = connection.channel()

ch.exchange_declare(exchange='second', exchange_type='fanout')
ch.queue_declare(queue='10angosht')
ch.queue_bind('10angosht', 'second')

def callback(ch, method, properties, body):
    print(f'Received {body}')

ch.basic_consume(queue='10angosht', on_message_callback=callback, auto_ack=True)
print('Start Consuming...')
ch.start_consuming()
