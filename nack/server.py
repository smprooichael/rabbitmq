import pika

credentials = pika.PlainCredentials('Meysam', 'maisam')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', credentials=credentials))
ch = connection.channel()

ch.exchange_declare('aj', exchange_type='fanout')
ch.queue_declare(queue='main')
ch.queue_bind('main', 'aj')

def callback(ch, method, properties, body):
    if method.delivery_tag % 5 == 0:
        ch.basic_nack(delivery_tag=method.delivery_tag, requeue=False, multiple= True)
    print(f'Received : {method.delivery_tag}')
    
ch.basic_consume(queue='main', on_message_callback=callback)
print('Starting consume...')
ch.start_consuming()