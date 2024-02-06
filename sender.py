import pika

credentials = pika.PlainCredentials('Meysam', 'maisam')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', credentials=credentials))
ch = connection.channel()

ch.queue_declare(queue='one')
ch.basic_publish(exchange='', routing_key='one', body='Hello world...')
print('Message was sent.')
connection.close()