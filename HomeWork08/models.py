from mongoengine import Document, StringField, ListField, BooleanField, DateTimeField, ReferenceField, connect


class Author(Document):
    fullname = StringField(required=True)
    born_date = StringField()
    born_location = StringField()
    description = StringField()


class Quote(Document):
    tags = ListField(StringField())
    author = ReferenceField(Author)
    quote = StringField()


class Contact(Document):
    fullname = StringField(required=True)
    email = StringField(required=True)
    phone_number = StringField()
    preferred_method = StringField(choices=['email', 'sms'], default='email')
    message_sent = BooleanField(default=False)