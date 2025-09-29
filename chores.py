import json
import sqlite3
from db import get_conn

FILE_PATH = 'chores.json'

def init_chores():
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute('DROP TABLE IF EXISTS Chores;')

    query = """
        CREATE TABLE CHORES (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Name VARCHAR(255) NOT NULL,
            Frequency VARCHAR(255) NOT NULL,
            GroupId INT NOT NULL,
            Score INT,
            isComplete BOOLEAN
        );
    """
    cursor.execute(query)

    print("~ Chores Table initiated")

def insert_chore(name, freq, groupId, score):
    conn = get_conn()
    cursor = conn.cursor()
    try:
        query = "INSERT INTO chores (name, frequency, groupId, score, isComplete) VALUES (?, ?, ?, ?, ?)"
        cursor.execute(query, (name, freq, groupId, score, False))
        conn.commit()
        print(f"Chore '{name}' added successfully.")
    except sqlite3.IntegrityError:
        print(f"Error: Chore named '{name}' already exists.")

def get_all_chores():
    conn = get_conn()
    cursor = conn.cursor()
    query = """
        SELECT * FROM chores 
        ORDER BY groupId
    """
    cursor.execute(query)
    return cursor.fetchall()

def seed_chores():
    with open(FILE_PATH, 'r') as f:
        data = json.load(f)

    for frequency, groups in data.items():
        for group, chores in groups.items():
            group_id = int(group)
            for chore in chores:
                insert_chore(chore, frequency, group_id, 0)

    print('~ Chores seeded')

def complete_chore(chore_id):
    conn = get_conn()
    cursor = conn.cursor()
    query = """
        UPDATE Chores 
        SET isComplete = TRUE
        WHERE ID = ?
    """
    cursor.execute(query, (chore_id,))
    conn.commit()
    conn.close()
