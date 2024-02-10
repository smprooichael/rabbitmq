import pika

credentials = pika.PlainCredentials('Meysam', 'maisam')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', credentials=credentials))
ch = connection.channel()

ch.exchange_declare(exchange='alt', exchange_type='fanout')
ch.exchange_declare(exchange='main', exchange_type='direct', arguments={'alternate-exchange':'alt'})

ch.queue_declare(queue='altq')
ch.queue_bind(exchange='alt', queue='altq')

ch.queue_declare(queue='mainq')
ch.queue_bind(exchange='main', queue='mainq', routing_key='home')

def alt_callback(ch, method, properties, body):
    print(f'Alt: received {body}')


def main_callback(ch, method, properties, body):
    print(f'Main: received {body}')

ch.basic_consume(queue='altq', on_message_callback=alt_callback, auto_ack=True)
ch.basic_consume(queue='mainq', on_message_callback=main_callback, auto_ack=True)

print('Start Consuming...')
ch.start_consuming()