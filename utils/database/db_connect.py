
#import sqlite3
#
#def create_con_db():
#    conn = sqlite3.connect('ig.bd')
#    cursor = conn.cursor()
#    create_db_sql = 'CREATE DATABASE {}'.format('1st_db')
#    cursor.execute(create_db_sql)
#    cursor.close()
#    conn.close()