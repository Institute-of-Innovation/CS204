import os

# List to store tasks
tasks = []

def show_menu():
    """Displays the To-Do List menu."""
    print("\nTo-Do List Menu:")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Mark Task as Done")
    print("5. Exit")

def view_tasks():
    """Displays the list of tasks."""
    if not tasks:
        print("No tasks available.")
    else:
        print("\nYour Tasks:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

def add_task():
    """Adds a new task to the list."""
    task = input("Enter a new task: ")
    tasks.append(task)
    print(f"Task '{task}' added successfully.")

def remove_task():
    """Removes a task based on user input."""
    view_tasks()
    try:
        task_number = int(input("Enter task number to remove: ")) - 1
        if 0 <= task_number < len(tasks):
            removed_task = tasks.pop(task_number)
            print(f"Task '{removed_task}' removed successfully.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def mark_task_done():
    """Marks a task as completed."""
    view_tasks()
    try:
        task_number = int(input("Enter task number to mark as done: ")) - 1
        if 0 <= task_number < len(tasks):
            tasks[task_number] += " ✔ (Done)"
            print("Task marked as completed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# Main program loop
while True:
    show_menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        view_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        remove_task()
    elif choice == "4":
        mark_task_done()
    elif choice == "5":
        print("Exiting... Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 5.")
