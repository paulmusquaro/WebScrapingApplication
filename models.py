from mongoengine import connect, Document, StringField, ReferenceField, ListField, CASCADE

host = "mongodb+srv://pavlokorjov9200:8Qw7iQEIIKekZtks@python9.j2j3njm.mongodb.net/"


connect(host=host, ssl=True)

class Author(Document):
    fullname = StringField(required=True, unique=True)
    born_date = StringField(max_length=50)
    born_location = StringField(max_length=150)
    description = StringField()
    meta = {"collection": "authors"}


class Quote(Document):
    author = ReferenceField(Author, reverse_delete_rule=CASCADE)
    tags = ListField(StringField(max_length=230))
    quote = StringField()
    meta = {"collection": "quotes"}
