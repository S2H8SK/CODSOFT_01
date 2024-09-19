import os

# File to store tasks
TODO_FILE = "todo_list.txt"

# Function to read tasks from file
def load_tasks():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, "r") as file:
            tasks = [line.strip() for line in file.readlines()]
        return tasks
    return []

# Function to save tasks to file
def save_tasks(tasks):
    with open(TODO_FILE, "w") as file:
        for task in tasks:
            file.write(task + "\n")

# Function to add a new task
def add_task():
    task = input("Enter a new task: ")
    tasks = load_tasks()
    tasks.append(task)
    save_tasks(tasks)
    print(f'Task "{task}" added.')

# Function to remove a task
def remove_task():
    tasks = load_tasks()
    if not tasks:
        print("No tasks to remove.")
        return
    for idx, task in enumerate(tasks, start=1):
        print(f"{idx}. {task}")
    task_num = int(input("Enter the task number to remove: "))
    if 1 <= task_num <= len(tasks):
        removed_task = tasks.pop(task_num - 1)
        save_tasks(tasks)
        print(f'Task "{removed_task}" removed.')
    else:
        print("Invalid task number.")

# Function to mark a task as complete
def complete_task():
    tasks = load_tasks()
    if not tasks:
        print("No tasks to complete.")
        return
    for idx, task in enumerate(tasks, start=1):
        print(f"{idx}. {task}")
    task_num = int(input("Enter the task number to mark as complete: "))
    if 1 <= task_num <= len(tasks):
        tasks[task_num - 1] += " [Completed]"
        save_tasks(tasks)
        print(f'Task "{tasks[task_num - 1]}" marked as complete.')
    else:
        print("Invalid task number.")

# Function to view tasks
def view_tasks():
    tasks = load_tasks()
    if tasks:
        print("Your To-Do List:")
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task}")
    else:
        print("No tasks in your to-do list.")

# Main menu function
def main_menu():
    while True:
        print("\nTo-Do List Menu:")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Mark Task as Complete")
        print("5. Exit")
        choice = input("Choose an option (1-5): ")

        if choice == "1":
            view_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            remove_task()
        elif choice == "4":
            complete_task()
        elif choice == "5":
            print("Exiting the To-Do List program. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

# Entry point
if __name__ == "__main__":
    main_menu()
