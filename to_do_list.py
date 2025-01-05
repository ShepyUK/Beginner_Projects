import json
tasks = []  # global tasks list

# Load tasks from file if it exists, otherwise create an empty file
try:
    with open("to_do_list.json", "r") as f:
        tasks = json.load(f)
        print("Tasks loaded:", tasks)
except FileNotFoundError:
    print("No existing to-do list found. Starting fresh.")
    with open("to_do_list.json", "w") as f:
        json.dump(tasks, f)


def save_tasks_to_file():  # saves tasks to file
    with open("to_do_list.json", "w") as f:
        json.dump(tasks, f)
    print("Tasks saved successfully!")


def show_menu():  # start menu
    print("\nWelcome to the To-Do List App!")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Complete")
    print("4. Delete Task")
    print("5. Exit")


def add_task():  # adds items to the to do list (1)
    task_name = input("Enter the task name: ")
    tasks.append({"name": task_name, "completed": False})
    save_tasks_to_file()
    print(f"Task '{task_name}' added successfully!")


def view_tasks():  # views tasks (2)
    if not tasks:
        print("No tasks avaliable.")
        return

    print("\nYour Tasks:")
    for i, task in enumerate(tasks, start=1):
        status = "completed" if task["completed"] else "pending"
        print(f"{i}. [ {status} ] {task['name']}")


def mark_task_complete():  # mark tasks as complete (3)
    if not tasks:
        print("No tasks available to mark as complete.")
        return

    view_tasks()
    try:
        task_number = int(input("Enter the task number to mark as complete: "))
        if 1 <= task_number <= len(tasks):
            tasks[task_number - 1]["completed"] = True
            save_tasks_to_file()
            print(f"Task '{tasks[task_number - 1]
                  ['name']}' marked as completed!")
        else:
            print("Invalid task number. Please Try again.")
    except ValueError:
        print("Invalid input. Please enter a number.")


def delete_task():  # delete tasks (4)
    if not tasks:
        print("No tasks available to delete.")
        return

    view_tasks()
    try:
        task_number = int(input("Enter the task number to delete: "))
        if 1 <= task_number <= len(tasks):
            removed_task = tasks.pop(task_number - 1)
            save_tasks_to_file()
            print(f"Task '{removed_task['name']}' has been deleted.")
        else:
            print("Invalid task number. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a number.")


def main():
    while True:
        show_menu()
        choice = input("Choose an options: ")

        if choice == "1":
            add_task()
            print("You chose to add a task.")
        elif choice == "2":
            view_tasks()
            print("you chose to view tasks.")
        elif choice == "3":
            mark_task_complete()
            print("you chose to mark a task as complete.")
        elif choice == "4":
            delete_task()
            print("you chose to delete a task.")
        elif choice == "5":
            print("Existing the app. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")


main()
