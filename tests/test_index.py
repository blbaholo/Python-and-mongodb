from mongoengine import connect, disconnect
import os
import pytest
from dotenv import load_dotenv, find_dotenv
from src.main import Visitor
from src.index import (
    create_visitor,
    delete_visitor,
    delete_all,
    list_visitors,
    update_visitor,
    visitor_details,
)

load_dotenv(find_dotenv(".env"))
disconnect()
connect("test_db", host=os.getenv("MONGO_TEST_HOST", "mongomock://localhost:9090"))


@pytest.fixture
def sample_document():
    create_visitor("Lerato", 22, "04/01/2023", "13:46", "Jacob", "Has great potential")
    return Visitor.objects.first()


def test_list_visitors():
    assert len(list_visitors()) == len(Visitor.objects())


def test_create_visitor(sample_document):
    assert sample_document.visitor_name == "Lerato"
    assert sample_document.visitor_age == 22
    assert sample_document.date_of_visit == "04/01/2023"
    assert sample_document.time_of_visit == "13:46"
    assert sample_document.name_of_person_who_assisted_the_visitor == "Jacob"
    assert sample_document.comments == "Has great potential"


def test_visitor_details(sample_document):
    assert visitor_details(sample_document.id) == {
        "id": sample_document.id,
        "name": "Lerato",
        "age": 22,
        "date_of_visit": "04/01/2023",
        "time_of_visit": "13:46",
        "name_of_person_who_assisted_the_visitor": "Jacob",
        "comments": "Has great potential",
    }


def test_update_visitor(sample_document):
    update_visitor(sample_document.id, date_of_visit="12/02/2023")
    visitor_object = Visitor.objects.first()
    assert visitor_object.date_of_visit == "12/02/2023"


def test_delete_visitor(sample_document):
    delete_visitor(sample_document.id)
    visitors = list_visitors()
    id_list = [visitor["id"] for visitor in visitors]
    assert sample_document.id not in id_list


def test_delete_all():
    create_visitor("Lerato", 22, "04/01/2023", "13:46", "Jacob", "Has great potential")
    delete_all()
    assert list_visitors() == []
