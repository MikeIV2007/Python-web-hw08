import random

from faker import Faker
import pika

from models import Contact
import connect

fake = Faker()

credentials = pika.PlainCredentials('guest', 'guest')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials))
channel = connection.channel()

channel.queue_declare(queue='email_queue')

channel.queue_declare(queue='sms_queue')

def generate_fake_contacts(count):
    fake_contacts = []
    for i in range(count):
        name = fake.name()
        email = fake.email()
        phone_number = fake.phone_number()
        contact_method = random.choice(['Email', 'SMS'])
        contact = Contact(full_name=name, email=email, phone_number=phone_number, preferred_contact_method=contact_method)
        contact.save()
        fake_contacts.append(contact)
    return fake_contacts

def send_contact_to_queue(contact, queue_name):
    channel.basic_publish(exchange='', routing_key=queue_name, body=str(contact.id))
    print(f"Contact {contact.id} sent to the {queue_name} queue")

if __name__ == '__main__':
    num_fake_contacts = 10
    fake_contacts = generate_fake_contacts(num_fake_contacts)
    
    for contact in fake_contacts:
        if contact.preferred_contact_method == 'Email':
            send_contact_to_queue(contact, 'email_queue')
        elif contact.preferred_contact_method == 'SMS':
            send_contact_to_queue(contact, 'sms_queue')

    connection.close()
