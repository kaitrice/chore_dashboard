from chores import complete_chore, get_all_chores, init_chores, reset_all_chores, rotate_chores, seed_chores
from db import get_all
from roommates import get_all_roommates, init_roommates, seed_roommates

init_chores()
seed_chores()

print('\n')

init_roommates()
seed_roommates()

def print_all_chores():
    rows = get_all_chores()

    if not rows:
        print("~ No chores found")
        return

    print("\n--- All Chores ---")
    for row in rows:
        name, frequency, group_id, score = row
        print(f"[Group {group_id}] ({frequency}) {name} | Score: {score}")

def print_all_roommates():
    rows = get_all_roommates()

    if not rows:
        print("~ No roommates found")
        return

    print("\n--- All Roommates ---")
    for row in rows:
        name, group_id, score = row
        print(f"{name} [Group {group_id}] | Score: {score}")

def print_all():
    rows = get_all()

    if not rows:
        print("~ No data found")
        return

    print("---  Chore Dashboard  ---")
    for row in rows:
        chore, roommate, isComplete = row
        print(f"{roommate} | {chore} {isComplete}")


# print_all_chores()
# print_all_roommates()
print_all()

print('\n\n')
complete_chore(2)
print_all()

print('\n\n')
reset_all_chores()
print_all()

print('\n\n')
rotate_chores()
print_all()
