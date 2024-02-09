import pika
from pika.exchange_type import ExchangeType

credentials = pika.PlainCredentials('Meysam', 'maisam')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', credentials=credentials))
ch = connection.channel()

ch.exchange_declare(exchange='he', exchange_type=ExchangeType.headers)

ch.basic_publish(exchange='he', routing_key='', body='Hello world!', properties=pika.BasicProperties(
                                                                                    headers={'name':"Meysam"}
))

print("Sent...")

ch.connection.close()