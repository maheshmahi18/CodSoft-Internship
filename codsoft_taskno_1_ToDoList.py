# Define an empty list to store tasks
tasks = []

# Function to display tasks
def display_tasks():
    if tasks:
        print("Your To-Do List:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")
    else:
        print("Your To-Do List is empty.")

# Function to add a task
def add_task(task):
    tasks.append(task)
    print(f"Task '{task}' added to your To-Do List.")

# Function to delete a task
def delete_task(task_index):
    if task_index >= 1 and task_index <= len(tasks):
        deleted_task = tasks.pop(task_index - 1)
        print(f"Task '{deleted_task}' deleted from your To-Do List.")
    else:
        print("Invalid task index.")

# Main program loop
while True:
    print("\nWelcome to the To-Do List App!")
    print("1. Display To-Do List")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        display_tasks()
    elif choice == "2":
        new_task = input("Enter the task to add: ")
        add_task(new_task)
    elif choice == "3":
        display_tasks()
        task_index = int(input("Enter the index of the task to delete: "))
        delete_task(task_index)
    elif choice == "4":
        print("Thank you for using the To-Do List App. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")