import sqlite3

DB_PATH = 'data/chores.db'

def get_conn():
    return sqlite3.connect(DB_PATH)

try:
    conn = get_conn()
    print("\n~ DB initiated")

except sqlite3.Error as e:
    print('~ Error occurred: ', e)

finally:
    if conn:
        conn.close()
        print('~ Database connection closed\n')
