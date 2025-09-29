from chores import get_all_chores, init_chores, seed_chores

init_chores()
seed_chores()

def print_all_chores():
    rows = get_all_chores()

    if not rows:
        print("~ No chores found")
        return

    print("\n--- All Chores ---")
    for row in rows:
        name, frequency, group_id, score = row
        print(f"[Group {group_id}] ({frequency}) {name} | Score: {score}")

print("---  Chore Dashboard  ---")

print_all_chores()
