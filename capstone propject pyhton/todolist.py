FILE_NAME = "tasks.txt"


def load_tasks():
    tasks = []
    try:
        with open(FILE_NAME, "r") as f:
            for line in f:
                line = line.strip()
                if line:
                    done, priority, title = line.split("|", 2)
                    tasks.append({
                        "title": title,
                        "done": done == "1",
                        "priority": priority
                    })
    except FileNotFoundError:
        pass
    return tasks


def save_tasks(tasks):
    with open(FILE_NAME, "w") as f:
        for t in tasks:
            f.write(f"{1 if t['done'] else 0}|{t['priority']}|{t['title']}\n")


def show_tasks(tasks):
    if len(tasks) == 0:
        print("\nNo tasks yet.")
        return
    print("\n--- Your To-Do List ---")
    for i in range(len(tasks)):
        status = "Done" if tasks[i]["done"] else "Pending"
        print(str(i + 1) + ". " + tasks[i]["title"] +
              " [" + status + "] (Priority: " + tasks[i]["priority"] + ")")


def add_task(tasks):
    title = input("Enter task: ").strip()
    if title == "":
        print("Task cannot be empty.")
        return
    priority = input("Priority (high/medium/low): ").strip().lower()
    if priority not in ["high", "medium", "low"]:
        priority = "medium"
    tasks.append({"title": title, "done": False, "priority": priority})
    save_tasks(tasks)
    print("Task added!")


def get_task_index(tasks, action):
    if len(tasks) == 0:
        print("\nNo tasks yet.")
        return -1
    show_tasks(tasks)
    num = input("Enter task number to " + action + ": ")
    if num.isdigit() and 1 <= int(num) <= len(tasks):
        return int(num) - 1
    print("Invalid task number.")
    return -1


def complete_task(tasks):
    idx = get_task_index(tasks, "mark as done")
    if idx != -1:
        tasks[idx]["done"] = True
        save_tasks(tasks)
        print("Task marked as completed!")


def edit_task(tasks):
    idx = get_task_index(tasks, "edit")
    if idx != -1:
        new_title = input("Enter new title: ").strip()
        if new_title != "":
            tasks[idx]["title"] = new_title
            save_tasks(tasks)
            print("Task updated!")
        else:
            print("Title cannot be empty.")


def delete_task(tasks):
    idx = get_task_index(tasks, "delete")
    if idx != -1:
        removed = tasks.pop(idx)
        save_tasks(tasks)
        print("Deleted:", removed["title"])


def main():
    tasks = load_tasks()
    while True:
        print("\n===== TO-DO LIST MANAGER =====")
        print("1. View tasks")
        print("2. Add task")
        print("3. Mark task as done")
        print("4. Edit task")
        print("5. Delete task")
        print("6. Exit")

        choice = input("Choose an option (1-6): ").strip()

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            edit_task(tasks)
        elif choice == "5":
            delete_task(tasks)
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")


main()