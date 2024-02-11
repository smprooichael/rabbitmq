import pika

credentials = pika.PlainCredentials('Meysam', 'maisam')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', credentials=credentials))
ch = connection.channel()

ch.exchange_declare(exchange='main', exchange_type='direct')
ch.basic_publish(exchange='main', routing_key='home', body='Hello world..!')

print("Sent...!")
connection.close()