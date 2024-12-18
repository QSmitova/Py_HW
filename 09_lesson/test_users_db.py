from sqlalchemy import create_engine, inspect
import pytest
import psycopg2
from sqlalchemy.sql import text


db_connection_string = "postgresql://postgres:0289@localhost:5432/QA"
engine = create_engine(db_connection_string)

def test_db_connection():
    try:
        engine = create_engine(db_connection_string)
        connection = engine.connect()

        assert connection is not None, "Соединение с базой данных не установлено"

        connection.close()
    except Exception as e:
        pytest.fail(f"ошибка подключения к базе данных: {e}")

def test_get_table():
    inspector = inspect(engine)
    names = inspector.get_table_names()  # Получаем список имен таблиц
    assert names[0] == 'users'

def test_insert():
    db = create_engine(db_connection_string)
    sql = text("insert into users(\"user_email\") values (:new_user_email)")
    with db.connect() as connection:  #
        connection.execute(sql, {"new_user_email": 'tsmit@ya.ru'})
        connection.commit()
        print(f"Создан новый пользователь")

def test_update():
    db = create_engine(db_connection_string)
    sql = text("update users set subject_id= :subj where user_email= :new_user_email")
    with db.connect() as connection:  #
        connection.execute(sql, {"subj": 2, "new_user_email": 'tsmit@ya.ru'})
        connection.commit()
        print(f"Данные пользователя отредактированы")

def test_delete():
    db = create_engine(db_connection_string)
    sql = text("delete from users where user_email= :new_user_email")
    with db.connect() as connection:  #
        connection.execute(sql, {"new_user_email": 'tsmit@ya.ru'})
        connection.commit()
        print(f"Пользователь удален")