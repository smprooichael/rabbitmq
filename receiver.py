import pika
import time

crednetials = pika.PlainCredentials('Meysam', 'maisam')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', credentials=crednetials))
ch = connection.channel()
ch.queue_declare(queue='one')

def callback(ch, method, properties, body):
    print(f'Received {body}')
    print(method)
    time.sleep(5)
    print("Done!")
    ch.basic_ack(delivery_tag=method.delivery_tag)

ch.basic_qos(prefetch_count=1)
ch.basic_consume(queue='one', on_message_callback=callback, auto_ack=True)
print('Waiting for messages. To exit press ctrl+c')
ch.start_consuming()