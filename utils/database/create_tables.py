import sqlite3
import mysql.connector
from mysql.connector import Error

def create_table():
    conn = sqlite3.connect('ig.bd')
    try:
        cursor = conn.cursor()
        create_table_users = '''
        CREATE TABLE IF NOT EXISTS users(
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        tg_id INTEGER NOT NULL,
        username TEXT,
        first_name TEXT,
        date_reg TEXT
        )'''
        cursor.execute(create_table_users)
        create_queue_table = '''
        CREATE TABLE IF NOT EXISTS queue(
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        number INTEGER NOT NULL)
        '''
        cursor.execute(create_queue_table)
        conn.commit()
    except Error as e:
        print(e)
    finally:
        cursor.close()
        conn.close()
