import pika

credentials = pika.PlainCredentials('Meysam', 'maisam')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', credentials=credentials))
ch = connection.channel()

ch.exchange_declare('aj', exchange_type='fanout')

while True:
    ch.basic_publish(exchange='aj', routing_key='home', body='Hello')
    print("Sent...!")
    input('Press Enter to continue..!')