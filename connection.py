import mysql.connector
from contextlib import contextmanager


@contextmanager
def create_connection():
    connection = mysql.connector.connect(host='127.0.0.1', user='root', password='pass123', database='students')
    yield connection
    connection.rollback()
    connection.close()
    print('Connection closed')