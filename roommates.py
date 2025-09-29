import sqlite3
from db import get_conn


def init_roommates():
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute('DROP TABLE IF EXISTS Roommates;')

    query = """
        CREATE TABLE roommates (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Name VARCHAR(255) NOT NULL,
            Score INT
        );
    """

    cursor.execute(query)

    print("~ Roommates Table initiated")

def insert_roommate(name):
    conn = get_conn()
    cursor = conn.cursor()
    try:
        query = "INSERT INTO roommates (name, score) VALUES (?, ?)"
        cursor.execute(query, (name, 0))
        conn.commit()
        print(f"'{name}' added successfully.")
    except sqlite3.IntegrityError:
        print(f"Error: Chore named '{name}' already exists.")

def get_all_roommates():
    conn = get_conn()
    cursor = conn.cursor()
    query = """
        SELECT * FROM roommates
    """
    cursor.execute(query)
    return cursor.fetchall()

def seed_roommates():
    insert_roommate('Kait')
    insert_roommate('Zoe')
    print('~ Roommates seeded')
