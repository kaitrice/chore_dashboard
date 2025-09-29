import sqlite3
from db import get_conn


def init_roommates():
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute('DROP TABLE IF EXISTS Roommates;')

    query = """
        CREATE TABLE roommates (
            Name VARCHAR(255) NOT NULL,
            groupId INT NOT NULL,
            Score INT
        );
    """

    cursor.execute(query)

    print("~ Roommates Table initiated")

def insert_roommate(name, groupId):
    conn = get_conn()
    cursor = conn.cursor()
    try:
        query = "INSERT INTO roommates (name, groupId, score) VALUES (?, ?, 0)"
        cursor.execute(query, (name, groupId))
        conn.commit()
        print(f"'{name}' added successfully.")
    except sqlite3.IntegrityError:
        print(f"Error: Chore named '{name}' already exists.")

def get_all_roommates():
    conn = get_conn()
    cursor = conn.cursor()
    query = """
        SELECT * FROM roommates 
        ORDER BY groupId
    """
    cursor.execute(query)
    return cursor.fetchall()

def seed_roommates():
    insert_roommate('Kait', 1)
    insert_roommate('Zoe', 2)
    print('~ Roommates seeded')
