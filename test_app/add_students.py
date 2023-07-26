import requests

from path.paths import Paths

students = [
    {'firstname': 'Peter', 'lastname': 'Heim', 'birthday': '01-01-1986', 'city': 'Frankfurt'},
    {'firstname': 'Markus', 'lastname': 'Heinrich', 'birthday': '09-03-1978', 'city': 'Darmstadt'},
    {'firstname': 'Karl', 'lastname': 'Mustermann', 'birthday': '05-08-1963', 'city': 'Friedberg'},
    {'firstname': 'Julian', 'lastname': 'Müller', 'birthday': '10-11-1973', 'city': 'Gießen'}
]


def send_students(list_with_students):
    for student in list_with_students:
        print(student)
        response = requests.post(Paths.ADD_STUDENT, data=student)
        print(response.json())


# send_students(students)


def get_student_for_lastname(lastname):
    response = requests.get(Paths.GET_STUDENT+lastname)
    print(response.json())


get_student_for_lastname('Mustermann')
get_student_for_lastname('Mustermann OR 1=1;')
