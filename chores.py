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
            RoommateId INT NOT NULL,
            Score INT,
            isComplete BOOLEAN
        );
    """
    cursor.execute(query)

    print("~ Chores Table initiated")

def insert_chore(name, freq, roommate_id, score):
    conn = get_conn()
    cursor = conn.cursor()
    try:
        query = "INSERT INTO chores (name, frequency, roommateId, score, isComplete) VALUES (?, ?, ?, ?, ?)"
        cursor.execute(query, (name, freq, roommate_id, score, False))
        conn.commit()
        print(f"Chore '{name}' added successfully.")
    except sqlite3.IntegrityError:
        print(f"Error: Chore named '{name}' already exists.")

def get_all_chores():
    conn = get_conn()
    cursor = conn.cursor()
    query = """
        SELECT * FROM chores 
        ORDER BY roommate_id
    """
    cursor.execute(query)
    return cursor.fetchall()

def seed_chores():
    with open(FILE_PATH, 'r') as f:
        data = json.load(f)

    for frequency, roommates in data.items():
        for roommate, chores in roommates.items():
            roommate_id = int(roommate)
            for chore in chores:
                insert_chore(chore, frequency, roommate_id, 0)

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
