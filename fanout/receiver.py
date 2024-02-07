import pika

credentials = pika.PlainCredentials('Meysam', 'maisam')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', credentials=credentials))
ch = connection.channel()

ch.exchange_declare(exchange='logs', exchange_type='fanout')
result = ch.queue_declare(queue='', exclusive=True)

ch.queue_bind(exchange='logs', queue=result.method.queue)
print('Waiting for messages...')
print(result.method.queue)


def callback(ch, method, properties, body):
    print(f"Received {body}")
    ch.basic_ack(delivery_tag=method.delivery_tag)


ch.basic_consume(queue=result.method.queue, on_message_callback=callback)
ch.start_consuming()