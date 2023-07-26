from pony import orm

from entity.studentEntity import StudentEntity
from publisher.sqlitePublisher import SqlitePublisher


class SqliteService:
    def get_students(self):
        with orm.db_session:
            student_entities = orm.select(
                student_entity for student_entity in StudentEntity)
            students = [student_entity.to_dict() for student_entity in student_entities]
        return students

    def get_student(self, lastname):
        with orm.db_session:
            student_entities = orm.select(
                student_entity for student_entity in StudentEntity if student_entity.lastname == lastname)
            students = [student_entity.to_dict() for student_entity in student_entities]
        return students

    def save_student_entity(self, student):
        return SqlitePublisher().store_student(student)
