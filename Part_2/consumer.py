import time

import pika

from models import Contact
import connect

credentials = pika.PlainCredentials('guest', 'guest')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials))
channel = connection.channel()

channel.queue_declare(queue='email_queue')

def send_email(contact_id):
    print(f"Sending email to Contact {contact_id}")
    time.sleep(2)
    print(f"Email sent to Contact {contact_id}")

def callback(ch, method, properties, body):
    contact_id = body.decode()
    contact = Contact.objects(id=contact_id).first()
    if contact:
        if not contact.email_sent:
            send_email(contact_id)
            contact.email_sent = True
            contact.save()
        else:
            print(f"Email already sent to Contact {contact_id}")
    else:
        print(f"Contact {contact_id} not found")

channel.basic_consume(queue='email_queue', on_message_callback=callback, auto_ack=True)

print('Waiting for messages. To exit, press CTRL+C')
channel.start_consuming()
