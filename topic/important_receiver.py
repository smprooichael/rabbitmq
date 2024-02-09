import pika

credentials = pika.PlainCredentials('Meysam', 'maisam')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', credentials=credentials))
ch = connection.channel()

ch.exchange_declare(exchange='topic_logs', exchange_type='topic')
result = ch.queue_declare(queue='', exclusive=True)


ch.queue_bind(queue=result.method.queue, exchange='topic_logs', routing_key='#.important')
def callback(ch, method, properties, body):
    with open('error_logs.log', 'a') as el:
        el.write(f'{str(body)} \n')



ch.basic_consume(queue=result.method.queue, on_message_callback=callback, auto_ack=True)

print('Waiting for messages...')
ch.start_consuming()