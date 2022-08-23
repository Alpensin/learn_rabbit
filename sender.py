import json

import pika
from read_examole_json import read_example_json


connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='salepoint_updates')

body = read_example_json()
channel.basic_publish(exchange='', routing_key='salepoint_updates', body=json.dumps(body))
print(" [x] Sent message")
connection.close()
