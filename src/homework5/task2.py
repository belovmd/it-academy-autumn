# Создайте декоратор, который хранит результаты вызовы
# функции (за все время вызовов, не только текущий
# запуск программы)


def dec(fun):
    from datetime import datetime
    import sqlite3

    # для проверки мб использована ':memory:'
    conn = sqlite3.connect('dbname.db')
    cur = conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS Results (
       FuncName TEXT,
       Date TEXT,
       Result TEXT);
    """)
    conn.commit()

    def wrapper():
        fun_name = fun.__name__
        date = str(datetime.now)
        result = fun()
        cur.execute("""INSERT INTO results
            VALUES(?, ?, ?);""", (fun_name, date, result))
        conn.commit()
        print("successful done")

    return wrapper


@dec
def fun_func():
    return 275


fun_func()
fun_func()
fun_func()
