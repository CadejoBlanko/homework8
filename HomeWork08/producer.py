import pika
from mongoengine import connect
from models import Contact
import json

connect('HomeWork08', host='mongodb+srv://Cadejo:0aGnluXd4Y56CviJ@homework08.lgshiv5.mongodb.net/?retryWrites=true&w=majority')

fake_contacts = [
    {"fullname": "John Doe", "email": "john.doe@example.com", "phone_number": "123456789", "preferred_method": "email"},
    {"fullname": "Jane Doe", "email": "jane.doe@example.com", "phone_number": "987654321", "preferred_method": "sms"}
]

for contact_data in fake_contacts:
    Contact(**contact_data).save()

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='email_queue')
channel.queue_declare(queue='sms_queue')

for contact in Contact.objects:
    message = {"contact_id": str(contact.id)}
    if contact.preferred_method == "email":
        channel.basic_publish(exchange='', routing_key='email_queue', body=json.dumps(message))
    elif contact.preferred_method == "sms":
        channel.basic_publish(exchange='', routing_key='sms_queue', body=json.dumps(message))

connection.close()