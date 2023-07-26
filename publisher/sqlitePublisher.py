from pony import orm

from entity.studentEntity import StudentEntity


class SqlitePublisher:
    def store_student(self, student):
        try:
            with orm.db_session:
                StudentEntity(
                    firstname=student["firstname"],
                    lastname=student["lastname"],
                    birthday=student["birthday"],
                    city=student["city"]
                )
                return {"Successful": "True"}
        except orm.TransactionIntegrityError as transaction_integrity_error:
            return {"Error": transaction_integrity_error}
