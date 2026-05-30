tasks = []

def show_tasks():
    print("\n===== 💕 To-Do List =====")
    if len(tasks) == 0:
        print("No tasks yet!")
    else:
        for i, task in enumerate(tasks):
            checkbox = "[✓]" if task["done"] else "[ ]"
            print(f"{i+1}. {checkbox} {task['task']}")
    print("=========================")

def add_task():
    name = input("Enter task: ")
    tasks.append({"task": name, "done": False})
    print("Task added! ✅")

def mark_done():
    show_tasks()
    try:
        num = int(input("Enter task number to mark as done: ")) - 1
        tasks[num]["done"] = True
        print("Marked as done! ✓")
    except:
        print("Invalid number, try again.")

def delete_task():
    show_tasks()
    try:
        num = int(input("Enter task number to delete: ")) - 1
        removed = tasks.pop(num)
        print(f'Deleted: {removed["task"]} 🗑️')
    except:
        print("Invalid number, try again.")

def main():
    print("💕 Welcome to your To-Do List! 💕")
    while True:
        print("\nWhat do you want to do?")
        print("1. View tasks")
        print("2. Add a task")
        print("3. Mark task as done")
        print("4. Delete a task")
        print("5. Quit")

        choice = input("\nEnter choice (1-5): ")

        if choice == "1":
            show_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            mark_done()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("Goodbye! 💕")
            break
        else:
            print("Invalid choice, try again.")

main()
