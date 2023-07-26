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
    return SqliteService().insert_student_from_json(student)


@app.route('/get/student<string:lastname>', methods=["GET"])
def get_student(lastname):
    return SqliteService().get_student(lastname)


@app.route('/databasequery<string:query>', methods=["GET"])
def database_query(query):
    return SqliteService().execute_query(query)

@app.route('/databaseescapequery<string:query>', methods=["GET"])
def database_escape_query(query):
    return SqliteService().execute_escape_query(query)


if __name__ == '__main__':
    app.run()
