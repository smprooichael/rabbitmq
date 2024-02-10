import pika
import uuid

credentials = pika.PlainCredentials('Meysam', 'maisam')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', credentials=credentials))
ch = connection.channel()

reply_queue = ch.queue_declare(queue='', exclusive=True)

def on_reply_message_receive(ch, method, properties, body):
    print(f'reply received {body}')


ch.basic_consume(queue=reply_queue.method.queue, on_message_callback=on_reply_message_receive, auto_ack=True)


ch.queue_declare(queue='request-queue')
cor_id = str(uuid.uuid4())
print(f'Sending Request: {cor_id}')

ch.basic_publish('', routing_key='request-queue', properties=pika.BasicProperties(
                                                                    reply_to=reply_queue.method.queue,
                                                                    correlation_id=cor_id),
                                                                    body='Can i request a reply?')

print('Starting Client....')
ch.start_consuming()