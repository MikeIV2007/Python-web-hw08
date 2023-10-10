import time

import pika

from models import Contact
import connect

credentials = pika.PlainCredentials('guest', 'guest')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials))
channel = connection.channel()

channel.queue_declare(queue='sms_queue')

def send_sms(contact_id):
    print(f"Sending SMS to Contact {contact_id}")
    time.sleep(2)
    print(f"SMS sent to Contact {contact_id}")

def callback(ch, method, properties, body):
    contact_id = body.decode()
    contact = Contact.objects(id=contact_id).first()
    if contact:
        if not contact.sms_sent:
            send_sms(contact_id)
            contact.sms_sent = True
            contact.save()
        else:
            print(f"SMS already sent to Contact {contact_id}")
    else:
        print(f"Contact {contact_id} not found")

channel.basic_consume(queue='sms_queue', on_message_callback=callback, auto_ack=True)

print('SMS Consumer: Waiting for messages. To exit, press CTRL+C')
channel.start_consuming()
