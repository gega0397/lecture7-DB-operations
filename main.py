import os
import sqlite3
from data_generator import generate_data
from queries import QUERIES

DB_NAME = "books"


def validate_db(db_name):
    if os.path.exists(db_name):
        os.remove(db_name)


class DBManager:

    @staticmethod
    def validate_db(db_name):
        if os.path.exists(db_name):
            os.remove(db_name)

    def __init__(self, db_name, delete_on_creation=True):
        self.db_name = db_name
        self.delete_on_creation = delete_on_creation

    def __enter__(self):

        if self.delete_on_creation:
            validate_db(self.db_name)

        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()

        self.cursor.execute(QUERIES["create_table"])

        return self.cursor

    def __exit__(self, exc_type, exc_value, traceback):

        self.conn.commit()
        self.cursor.close()
        self.conn.close()


if __name__ == "__main__":
    with DBManager(DB_NAME) as cursor:
        data = generate_data(10)

        cursor.executemany(QUERIES["insert_many"], data)

        cursor.execute(QUERIES["get_average_length"])

        print(int(cursor.fetchone()[0]))

        cursor.execute(QUERIES["get_max_length"])

        print(cursor.fetchone()[0])
