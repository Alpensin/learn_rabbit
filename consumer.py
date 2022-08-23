import json

import pika

from schema import SalepointChangesSchema

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='salepoint_updates')


# def callback(ch, method, properties, body):
#     loaded_data = json.loads(body)
#     schema = SalepointChangesSchema()
#     result = schema.load(loaded_data)
#     print(result)

def callback(body):
    loaded_data = json.loads(body)
    schema = SalepointChangesSchema()
    result = schema.load(loaded_data)
    print(result)


channel.basic_consume(queue='salepoint_updates',
                      auto_ack=True,
                      on_message_callback=callback)
channel.start_consuming()

method_frame, header_frame, body = channel.basic_get('salepoint_updates')
if method_frame:
    print(method_frame, header_frame, body)
    channel.basic_ack(method_frame.delivery_tag)
    callback(body)
    channel.basic_ack()
else:
    print('No message returned')
