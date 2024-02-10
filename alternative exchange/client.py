import pika

credentials = pika.PlainCredentials('Meysam', 'maisam')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', credentials=credentials))
ch = connection.channel()

ch.exchange_declare(exchange='alt', exchange_type='fanout')
ch.exchange_declare(exchange='main', exchange_type='direct', arguments={'alternate-exchange':'alt'})

ch.basic_publish(exchange='main', routing_key='bad', body='Hello world!')

print('Sent...!')
ch.connection.close()
