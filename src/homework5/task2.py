"""
Создайте декоратор, который хранит результаты вызовы функции
(за все время вызовов, не только текущий запуск программы)
"""
import sqlite3 as lite
from datetime import datetime


DATABASE_FILE = "test.db"

SQL_CREATE_TABLE = """ CREATE TABLE IF NOT EXISTS Logs (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name text,
                        date text,
                        result text
                        ); """

SQL_INSERT_LOG = """ INSERT INTO Logs (NAME,DATE,RESULT) 
                     Values(\"{name}\",\"{date}\",\"{result}\")
                 """

SQL_FETCH_LOGS = """ SELECT * FROM Logs """


def database_connect(db_func):
    def connection_wraper(*args, **kwargs):
        try:
            conn = lite.connect(DATABASE_FILE)
            db_func(conn, *args, **kwargs)
        finally:
            conn.close()
    return connection_wraper


def amazing_decorator(gorgeous_func):
    create_table_if_not_exist()

    def super_wraper(*args, **kwargs):
        func_result = gorgeous_func(*args, **kwargs)
        log_func(gorgeous_func, func_result)
        print_logs()
    return super_wraper


@database_connect
def create_table_if_not_exist(conn):
    conn.cursor().execute(SQL_CREATE_TABLE)


@database_connect
def log_func(conn, gorgeous_func, result):
    curr_time = datetime.now().__str__()
    func_name = gorgeous_func.__name__
    request = SQL_INSERT_LOG.format(name=func_name,
                                    date=curr_time,
                                    result=result)
    cursor = conn.cursor()
    cursor.execute(request)
    conn.commit()


@database_connect
def print_logs(conn):
    cursor = conn.cursor()
    cursor.execute(SQL_FETCH_LOGS)
    logs = cursor.fetchall()
    print(logs)


@amazing_decorator
def func_for_logging():
    return


func_for_logging()
