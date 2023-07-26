import json

import mysql.connector
from mysql.connector import Error
from datetime import date, datetime
import pymysql
class SqliteService:

    def __init__(self):
        self.connection = self.create_database_connection(host_name='localhost',
                                                          user_name='root',
                                                          user_password='achilleus',
                                                          db_name='test')

    def create_database_connection(self, host_name, user_name, user_password, db_name):
        connection = None
        try:
            connection = mysql.connector.connect(
                host=host_name,
                user=user_name,
                passwd=user_password,
                database=db_name
            )
            print("SQL Database Connection succesful")
        except Error as err:
            print(f"Error: '{err}'")
        return connection

    def return_as_json(self, cursor, rows):
        columns = [x[0] for x in cursor.description]
        table_objects = []
        for row in rows:
            entry = {}
            for column, val in zip(columns, row):
                if isinstance(val, (datetime, date)):
                    val = val.isoformat()
                entry[column] = val
            table_objects.append(entry)
        return json.dumps(table_objects)

    def execute_query(self, query):
        cursor = self.connection.cursor()
        try:
            cursor.execute(query)
            rows = cursor.fetchall()
            print(rows)
            print("Query executed")
            return self.return_as_json(cursor, rows)
        except Error as error:
            print(f"Error: '{error}'")

    def execute_escape_query(self, query):
        cursor = self.connection.cursor()
        print(query)
        try:
            escaped_query = pymysql.escape_string(query)  # Escaping durchführen
            print(escaped_query)
            cursor.execute(escaped_query)
            rows = cursor.fetchall()
            print(rows)
            print("Query executed")
            return self.return_as_json(cursor, rows)
        except Error as error:
            print(f"Error: '{error}'")

    def insert_student_from_json(self, student):
        id_ = student['id']
        firstname_ = student['firstname']
        lastname_ = student['lastname']
        birthday_ = student['birthday']
        city_ = student['city']
        query = """ 
        INSERT INTO students (id, firstname, lastname, birthday, city)
        VALUES (%s, %s, %s, %s, %s)
        """
        val = (id_, firstname_, lastname_, birthday_, city_)
        cursor = self.connection.cursor()
        try:
            cursor.execute(query, val)
            self.connection.commit()
            print("Query executed")
            return {'Succesful ':student}
        except Error as error:
            print(f"Error: '{error}'")
