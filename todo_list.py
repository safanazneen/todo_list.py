
def display_tasks(tasks):
    print("\n===== YOUR TO-DO LIST =====")

    if not tasks:
        print("No tasks added yet.")
        return

    for number, task in enumerate(tasks, start=1):
        status = "Completed" if task["completed"] else "Pending"
        print(f"{number}. {task['title']} - {status}")

    print("===========================\n")


def add_task(tasks):
    title = input("Enter your task: ").strip()

    if not title:
        print("Task cannot be empty.")
        return

    tasks.append({"title": title, "completed": False})
    print("Task added successfully!")


def mark_completed(tasks):
    if not tasks:
        print("No tasks available to complete.")
        return

    display_tasks(tasks)
    choice = input("Enter the task number to complete: ").strip()

    if not choice.isdigit():
        print("Please enter a valid number.")
        return

    number = int(choice)

    if number < 1 or number > len(tasks):
        print("Invalid task number.")
        return

    tasks[number - 1]["completed"] = True
    print("Task marked as completed!")


def delete_task(tasks):
    if not tasks:
        print("No tasks available to delete.")
        return

    display_tasks(tasks)
    choice = input("Enter the task number to delete: ").strip()

    if not choice.isdigit():
        print("Please enter a valid number.")
        return

    number = int(choice)

    if number < 1 or number > len(tasks):
        print("Invalid task number.")
        return

    removed_task = tasks.pop(number - 1)
    print(f"Deleted task: {removed_task['title']}")


def main():
    tasks = []

    while True:
        print("\n===== PYTHON TO-DO LIST =====")
        print("1. Add a task")
        print("2. Display tasks")
        print("3. Mark a task as completed")
        print("4. Delete a task")
        print("5. Exit")

        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            display_tasks(tasks)
        elif choice == "3":
            mark_completed(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Thank you for using the To-Do List App!")
            break
        else:
            print("Invalid choice. Please select 1 to 5.")


if __name__ == "__main__":
    main()
