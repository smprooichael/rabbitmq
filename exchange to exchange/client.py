import pika

credentials = pika.PlainCredentials('Meysam', 'maisam')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', credentials=credentials))
ch = connection.channel()

ch.exchange_declare(exchange='first', exchange_type='direct')
ch.exchange_declare(exchange='second', exchange_type='fanout')
ch.exchange_bind('second', 'first')


ch.basic_publish(exchange='first', routing_key='', body='Hello world!')

print('Sent..!')
connection.close()