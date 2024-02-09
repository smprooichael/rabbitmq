import pika

credentials = pika.PlainCredentials("Meysam", "maisam")
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', credentials=credentials))
ch = connection.channel()

ch.exchange_declare(exchange='topic_logs', exchange_type='topic')

messages = {
    'error.logs.important': 'This is an important message',
    'info.error.notimportant': 'This is not an important message'
}

for k,v in messages.items():
    ch.basic_publish(exchange='topic_logs', routing_key=k, body=v)

print("Message...")
ch.connection.close()