from mongoengine import Document, connect, StringField, IntField
import os
from dotenv import load_dotenv, find_dotenv


load_dotenv(find_dotenv(".env"))
connect(db="UmuziProspects", host=os.getenv("MONGO_HOST", "mongodb://localhost:27017"))


class Visitor(Document):
    visitor_name = StringField(required=True, max_length=20)
    visitor_age = IntField(required=True)
    date_of_visit = StringField(required=True, max_length=20)
    time_of_visit = StringField(required=True, max_length=20)
    name_of_person_who_assisted_the_visitor = StringField(required=True, max_length=20)
    comments = StringField(required=True, max_length=50)
