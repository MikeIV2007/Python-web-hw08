from mongoengine import *
from mongoengine.fields import ListField, StringField, ReferenceField

    
class Author(Document):
    fullname = StringField(required=True)
    born_date = StringField(max_length=50)
    born_location = StringField(max_length=50)
    description = StringField()
    meta = {'allow_inheritance': True}


class Quote(Document):
    tags = ListField(StringField(max_length=30))
    author = ReferenceField(Author, reverse_delete_rule=CASCADE)
    quote = StringField(max_length=150, required=True)
    meta = {'allow_inheritance': True}