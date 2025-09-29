from chores import complete_chore, list_chores, init_chores, reset_all_chores, rotate_chores, seed_chores
from db import get_all
from roommates import complete_chore_for_roommate, list_roommates, init_roommates, seed_roommates
from utils import isSunday

init_chores()
seed_chores()

print('\n')

init_roommates()
seed_roommates()

def print_chores():
    rows = list_chores()

    if not rows:
        print("~ No chores found")
        return

    print("\n--- All Chores ---")
    for row in rows:
        name, frequency, id, score = row
        print(f"[Group {id}] ({frequency}) {name} | Score: {score}")

def print_roommates():
    rows = list_roommates()

    if not rows:
        print("~ No roommates found")
        return

    print("\n--- All Roommates ---")
    for row in rows:
        name, id, score = row
        print(f"{name} [ID {id}] | Score: {score}")

def print_all():
    rows = get_all()

    if not rows:
        print("~ No data found")
        return

    print("---  Chore Dashboard  ---")
    for row in rows:
        chore, roommate, score, isComplete = row
        print(f"{roommate} - {score} | {chore} {isComplete}")


# print_chores()
# print_roommates()
print_all()

print('\n\n')
complete_chore_for_roommate(1,1)
print_all()

# print('\n\n')
# reset_all_chores()
# print_all()

# print('\n\n')
# rotate_chores()
# print_all()

# print(isSunday())