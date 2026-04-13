import json

FILE_NAME = "habits.json"

# Load habits if file exists
def load_habits():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except:
        return []

# Save habits to JSON
def save_habits(habits_list):
    with open(FILE_NAME, "w") as file:
        json.dump(habits_list, file, indent=4)


habits = load_habits()

# Each habit:
# {
#     "name": str,
#     "target_per_week": int,
#     "total": int,
#     "log": [1, 1, 1]
# }


def show_menu():
    print("\n--- HABIT TRACKER ---")
    print("1. Add habit")
    print("2. Log today")
    print("3. Show habits")
    print("4. Show summary")
    print("5. Save and Exit")
    return input("Choose (1-5): ")


def add_habit(habits_list):
    name = input("Habit name: ")
    target = int(input("Target per week: "))

    habit = {
        "name": name,
        "target_per_week": target,
        "total": 0,
        "log": []
    }

    habits_list.append(habit)
    print("Habit added.")


def log_today(habits_list):
    if len(habits_list) == 0:
        print("No habits yet.")
        return

    for i in range(len(habits_list)):
        print(f"{i + 1}. {habits_list[i]['name']}")

    choice = int(input("Choose habit number: "))

    if 1 <= choice <= len(habits_list):
        answer = input("Completed today? (y/n): ").lower()

        if answer == "y":
            habits_list[choice - 1]["total"] += 1
            habits_list[choice - 1]["log"].append(1)
            print("Logged")
        else:
            print("Not logged.")
    else:
        print("Invalid choice.")


def show_habits(habits_list):
    if len(habits_list) == 0:
        print("No habits yet.")
        return

    print("\nHabit".ljust(15), "Target".ljust(10), "Total")
    print("-" * 30)

    for habit in habits_list:
        print(
            habit["name"].ljust(15),
            str(habit["target_per_week"]).ljust(10),
            habit["total"]
        )


def show_summary(habits_list):
    if len(habits_list) == 0:
        print("No habits yet.")
        return

    print("\n--- SUMMARY ---")

    for habit in habits_list:
        total = habit["total"]
        target = habit["target_per_week"]

        if target > 0:
            rate = (total / target) * 100
        else:
            rate = 0

        print(f"{habit['name']}: {total} completions ({rate:.0f}% of target)")


while True:
    choice = show_menu()

    if choice == "1":
        add_habit(habits)

    elif choice == "2":
        log_today(habits)

    elif choice == "3":
        show_habits(habits)

    elif choice == "4":
        show_summary(habits)

    elif choice == "5":
        save_habits(habits)
        print("Habits saved. Goodbye.")
        break

    else:
        print("Invalid input.")
