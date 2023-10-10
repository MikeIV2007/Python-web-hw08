from mongoengine import Document, StringField, BooleanField

class Contact(Document):
    full_name = StringField(required=True)
    email = StringField(required=True)
    phone_number = StringField(required=True)
    email_sent = BooleanField(default=False)
    sms_sent = BooleanField(default=False)
    preferred_contact_method = StringField(choices=['Email', 'SMS'], default='Email')
