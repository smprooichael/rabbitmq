import pika
import time

credentials = pika.PlainCredentials('Meysam', 'maisam')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', credentials=credentials))
ch = connection.channel()

ch.queue_declare(queue='one')
ch.basic_publish(exchange='', routing_key='one', body='Hello world...', properties=pika.BasicProperties(
    content_type="text/plain",
    content_encoding="gzip",
    timestamp=10000000,
    expiration=str(time.time()),
    user_id="10",
    app_id="11",
    type="exch.queue",
    delivery_mode=2,
    headers={"name":"meysam", "age":"23"},
))
print('Message was sent.')
connection.close()