import sqlite3

DB_PATH = 'database.db'

def get_conn():
    return sqlite3.connect(DB_PATH)

def close_connection():
    conn = get_conn()
    if conn:
        conn.close()
        print('~ Database connection closed\n')

def get_all():
    conn = get_conn()
    cursor = conn.cursor()
    query = """
        SELECT chores.name as Chore, roommates.name as Roommate, isComplete
        FROM Chores
        JOIN Roommate ON chores.groupId = roommates.groupId
        ORDER BY roommate
    """
    cursor.execute(query)
    return cursor.fetchall()

try:
    conn = get_conn()
    print("\n~ DB initiated")

except sqlite3.Error as e:
    print('~ Error occurred: ', e)

finally:
    close_connection()