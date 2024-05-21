import sqlite3
from bot import bot
from mysql.connector import Error
from config import BOT_ADMIN

def add_new_user(tg_id, username, first_name, date_reg):
    try:
        conn = sqlite3.connect('ig.bd')
        cursor = conn.cursor()
        new_user = f'''
        INSERT INTO
        users (tg_id, username, first_name, date_reg)
        VALUES
        ('{tg_id}','{username}','{first_name}','{date_reg}'); '''
        cursor.execute(new_user)
        conn.commit()
        add_result = f'''Новый юзер {username} добавлен в бд'''
        print(add_result)
    except Error as e:
        print(f'''Ошибка {e}''')
    finally:
        cursor.close()
        conn.close()

def add_new_queue(number):
    try:
        conn = sqlite3.connect('ig.bd')
        cursor = conn.cursor()
        last_user = f'''INSERT INTO queue (number) VALUES ('{number}');'''
        cursor.execute(last_user)
        conn.commit()
    except Error as e:
        print(f'''Ошибка {e}''')
    finally:
        cursor.close()
        conn.close()

def add_to_queue(number):
    try:
        conn = sqlite3.connect('ig.bd')
        cursor = conn.cursor()
        last_user = f'''UPDATE queue SET number={number} WHERE id = 1'''
        cursor.execute(last_user)
        conn.commit()
    except Error as e:
        print(f'''Ошибка {e}''')
    finally:
        cursor.close()
        conn.close()

def check_queue():
    try:
        conn = sqlite3.connect('ig.bd')
        cursor = conn.cursor()
        check_last = f'''SELECT number FROM queue ORDER BY id DESC LIMIT 1'''
        check = cursor.execute(check_last)
        result = check.fetchone()
        return result
    except Error as e:
        print(f'''Ошибка {e}''')
    finally:
        cursor.close()
        conn.close()


def reset_queue():
    try:
        conn = sqlite3.connect('ig.bd')
        cursor = conn.cursor()
        last_user = f'''UPDATE queue SET number=0 WHERE id = 1'''
        cursor.execute(last_user)
        conn.commit()
    except Error as e:
        print(f'''Ошибка {e}''')
    finally:
        cursor.close()
        conn.close()

def delete_queue():
    try:
        conn = sqlite3.connect('ig.bd')
        cursor = conn.cursor()
        check_last = f'''DELETE FROM queue WHERE id = 2'''
        check = cursor.execute(check_last)
        conn.commit()

    except Error as e:
        print(f'''Ошибка {e}''')
    finally:
        cursor.close()
        conn.close()

def show_queue():
    try:
        conn = sqlite3.connect('ig.bd')
        cursor = conn.cursor()
        check_last = f'''SELECT * FROM queue'''
        check = cursor.execute(check_last)
        result = check.fetchall()
        return result
    except Error as e:
        print(f'''Ошибка {e}''')
    finally:
        cursor.close()
        conn.close()

def show_all_users():
    try:
        conn = sqlite3.connect('ig.bd')
        cursor = conn.cursor()
        request = f'''SELECT * FROM users'''
        show_users = cursor.execute(request)
        result = show_users.fetchall()
        return result
    except Error as e:
        print(f'''Ошибка {e}''')
    finally:
        cursor.close()
        conn.close()