from src.main import Visitor


def create_visitor(name, age, date, time, name_of_person_who_assisted, comments):
    visitor = Visitor(
        visitor_name=name,
        visitor_age=age,
        date_of_visit=date,
        time_of_visit=time,
        name_of_person_who_assisted_the_visitor=name_of_person_who_assisted,
        comments=comments,
    )
    visitor.save()


def list_visitors():
    list_of_visitors = [
        {"id": str(visitor.id), "name": visitor.visitor_name}
        for visitor in Visitor.objects
    ]
    return list_of_visitors


def update_visitor(id, **updates):
    Visitor.objects(id=id).update(**updates)


def visitor_details(id):
    for visitor in Visitor.objects(id=id):
        return {
            "id": visitor.id,
            "name": visitor.visitor_name,
            "age": visitor.visitor_age,
            "date_of_visit": visitor.date_of_visit,
            "time_of_visit": visitor.time_of_visit,
            "name_of_person_who_assisted_the_visitor": visitor.name_of_person_who_assisted_the_visitor,
            "comments": visitor.comments,
        }


def delete_visitor(id):
    Visitor.objects(id=id).delete()


def delete_all():
    Visitor.objects.delete()
