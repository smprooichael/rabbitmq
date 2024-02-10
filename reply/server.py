import pika

credentials = pika.PlainCredentials('Meysam', 'maisam')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', credentials=credentials))
ch = connection.channel()

ch.queue_declare(queue='request-queue')


def on_request_message_received(ch, method, properties, body):
    print(f'Received request: {properties.correlation_id}')
    ch.basic_publish('', routing_key=properties.reply_to, body=f'Reply to {properties.correlation_id}')

ch.basic_consume(queue='request-queue', auto_ack=True, on_message_callback=on_request_message_received)

print('Starting server...!')
ch.start_consuming()