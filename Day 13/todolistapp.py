def display_menu():
    print("\n===== To-Do List Menu =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Done")
    print("4. Remove Task")
    print("5. Exit")

def add_task(tasks):
    task = input("Enter the task: ")
    tasks.append({"task": task, "done": False})
    print(f"Task '{task}' added!")

def view_tasks(tasks):
    if not tasks:
        print("No tasks in the list.")
    else:
        print("\nYour To-Do List:")
        for idx, task in enumerate(tasks, start=1):
            status = "Done" if task["done"] else "Not Done"
            print(f"{idx}. {task['task']} - {status}")

def mark_task_done(tasks):
    view_tasks(tasks)
    try:
        task_num = int(input("Enter the task number to mark as done: "))
        if 0 < task_num <= len(tasks):
            tasks[task_num - 1]["done"] = True
            print(f"Task {task_num} marked as done!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def remove_task(tasks):
    view_tasks(tasks)
    try:
        task_num = int(input("Enter the task number to remove: "))
        if 0 < task_num <= len(tasks):
            removed_task = tasks.pop(task_num - 1)
            print(f"Task '{removed_task['task']}' removed!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def to_do_list_app():
    tasks = []
    while True:
        display_menu()
        choice = input("Choose an option: ")
        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            mark_task_done(tasks)
        elif choice == '4':
            remove_task(tasks)
        elif choice == '5':
            print("Exiting the To-Do List application. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    to_do_list_app()
