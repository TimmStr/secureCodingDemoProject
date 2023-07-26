import requests

from path.paths import Paths

students = [
    {'id': 1, 'firstname': 'Peter', 'lastname': 'Heim', 'birthday': '1986-01-01', 'city': 'Frankfurt'},
    {'id': 2, 'firstname': 'Markus', 'lastname': 'Heinrich', 'birthday': '1978-09-03', 'city': 'Darmstadt'},
    {'id': 3, 'firstname': 'Karl', 'lastname': 'Mustermann', 'birthday': '1963-05-08', 'city': 'Friedberg'},
    {'id': 4, 'firstname': 'Julian', 'lastname': 'Müller', 'birthday': '1973-10-11', 'city': 'Gießen'}
]


def insert_students(list_with_students):
    for student in list_with_students:
        print(student)
        response = requests.post(Paths.ADD_STUDENT, data=student)
        print(response.json())


# insert_students(students)


def test_query():
    # response = requests.get(Paths.DATABASE_QUERY + " SELECT * FROM students")
    response = requests.get(Paths.DATABASE_ESCAPE_QUERY + " SELECT * FROM students WHERE firstname='Peter'")# OR 1=1")
    print(response.json())


test_query()
