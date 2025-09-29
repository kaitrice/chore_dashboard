from chores import complete_chore, get_chore, get_chores, init_chores, reset_all_chores, rotate_chores, seed_chores
from db import get_all
from roommates import complete_chore_for_roommate, get_roommate, get_roommates, init_roommates, seed_roommates
from utils import isSunday

def list_chores():
    rows = get_chores()

    if not rows:
        print("~ No chores found")
        return

    print("\n--- All Chores ---")
    for row in rows:
        id_, name, frequency, roommate_id, score, is_complete = row
        print(f"[{id_}] Group {roommate_id} | {name} ({frequency}) | Completed: {is_complete} | Score: {score}")

def list_roommates():
    rows = get_roommates()

    if not rows:
        print("~ No roommates found")
        return

    print("\n--- All Roommates ---")
    for row in rows:
        id_, name, score = row
        print(f"[{id_}] | Score: {score} | {name}")

def list_all():
    rows = get_all()

    if not rows:
        print("~ No data found")
        return

    print("---  Chore Dashboard  ---")
    for row in rows:
        chore, roommate, score, isComplete = row
        print(f"{roommate} - {score} | {chore} {isComplete}")

def help():
    print("\nAvailable Commands:")
    print("-------------------")
    print(" a : List all items")
    print(" c : List chores")
    print(" r : List roommates")
    print(" u chore_id roommate_id : Complete chore for roommate")
    print(" h : Show this help menu")
    print(" q : Quit the program")

# list_chores()
# list_roommates()
# list_all()

# print('\n\n')
# complete_chore_for_roommate(1,1)
# list_all()

# print('\n\n')
# reset_all_chores()
# list_all()

# print('\n\n')
# rotate_chores()
# list_all()

# print(isSunday())

init_chores()
seed_chores()
print('\n')
init_roommates()
seed_roommates()

print('\n\n')
print("Starting up dashboard...")
## CREATE CLI dashboard
cmd = ""
while cmd != "q":
    cmd = input("* ")
    match cmd[0]:
        case "h":
            help()
        case "a":
            list_all()
        case "c":
            list_chores()
        case "r":
            list_roommates()
        case "u":
            chore_id = cmd[2]
            roommate_id = cmd[4]

            complete_chore_for_roommate(chore_id, roommate_id)

            chore = get_chore(chore_id)
            chore_name = chore[1]
            score = chore[4]
            person = get_roommate(roommate_id)
            person_name = person[1]

            print(f"Chore '{chore_name}' updated for roommate '{person_name}' +'{score}'")

    print('\n')
    