import pika
import time

credentials = pika.PlainCredentials('Meysam', 'maisam')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', credentials=credentials))
ch = connection.channel()

ch.exchange_declare(exchange='main', exchange_type='direct', durable=True, auto_delete=False)
ch.queue_declare(queue='mainq', durable=True, auto_delete=False, exclusive=False)
ch.queue_bind('mainq', 'main', 'home')

ch.confirm_delivery()

for i in range(20):
    try:
        ch.basic_publish(exchange='main', routing_key='home', body='Hello World!', properties=pika.BasicProperties(
                                                                                    content_type='text/plain',
                                                                                    delivery_mode=2)
        , mandatory=True)
        print(f'Message {i} confirmed...')
    except Exception as e:
        print(f'Exception: {type(e).__name__}')
    time.sleep(2)