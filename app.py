from flask import Flask
from flask import request
from service.sqliteService import SqliteService

app = Flask(__name__)


@app.route('/')
def get_students():
    return SqliteService().get_students()


@app.route('/add/student', methods=["POST"])
def add_student():
    student = request.values
    return SqliteService().save_student_entity(student)

@app.route('/get/student<string:lastname>', methods=["GET"])
def get_student(lastname):
    return SqliteService().get_student(lastname)


if __name__ == '__main__':
    app.run()
