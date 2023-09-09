import pika
from mongoengine import connect
from models import Contact
import json

connect('HomeWork08', host='mongodb+srv://Cadejo:0aGnluXd4Y56CviJ@homework08.lgshiv5.mongodb.net/?retryWrites=true&w=majority')

def send_email(contact_id):
    pass

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='email_queue')

def callback(ch, method, properties, body):
    message = json.loads(body)
    contact_id = message['contact_id']
    contact = Contact.objects.get(id=contact_id)

    send_email(contact_id)

    
    contact.message_sent = True
    contact.save()


channel.basic_consume(queue='email_queue', on_message_callback=callback, auto_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()