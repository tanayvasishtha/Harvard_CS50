import sys
from datetime import datetime

tasks = []

def main():
    while True:
        print("\nTask Management System")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Complete")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            add_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            mark_task_complete()
        elif choice == '4':
            print("Thank you for using the Task Management System!")
            sys.exit()
        else:
            print("Invalid choice. Please try again.")

def add_task():
    task = input("Enter task description: ")
    due_date = input("Enter due date (YYYY-MM-DD): ")
    try:
        due_date = datetime.strptime(due_date, "%Y-%m-%d")
        tasks.append({"description": task, "due_date": due_date, "completed": False})
        print("Task added successfully!")
    except ValueError:
        print("Invalid date format. Task not added.")

def view_tasks():
    if not tasks:
        print("No tasks found.")
    else:
        for i, task in enumerate(tasks, 1):
            status = "Completed" if task["completed"] else "Pending"
            print(f"{i}. {task['description']} - Due: {task['due_date'].strftime('%Y-%m-%d')} - Status: {status}")

def mark_task_complete():
    view_tasks()
    if tasks:
        try:
            task_num = int(input("Enter the task number to mark as complete: ")) - 1
            if 0 <= task_num < len(tasks):
                tasks[task_num]["completed"] = True
                print("Task marked as complete!")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()
