tasks_file = "tasks.txt"

def loadTasks():
    try:
        with open(tasks_file, "r") as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        return []
    
def saveTasks():
    with open(tasks_file, "w") as file:
        for task in tasks:
            file.write(task + "\n")

tasks = loadTasks()

def addTask():
    task = input("Enter a new task: ")
    tasks.append(task)
    saveTasks()
    print("task added successfully")

def deleteTasks():
    if len(tasks) == 0:
        print("no task to delete")
    else:
        for i, task in enumerate(tasks):
            print(f'{i+1}. {task}')
        choice = int(input("Enter the task number to delete: "))
        if choice <= len(tasks):
            del tasks[choice -1]
            saveTasks()
            print("selected task deleted successfully.\n")
        else:
            print("Invalid task number.\n")

def viewTasks():
    if len(tasks) == 0:
        print("No tasks to show.\n")
    else:
        print("Here are the number of tasks.\n")
        for i, task in enumerate(tasks):
            print(f'{i+1}. {task}')


def main():
    while True:
        print("\n==========================To-Do Web Application==========================")
        print("1. Add Task")
        print("2. Delete Task")
        print("3. View Tasks")
        print("4. Exit\n")
        
        choice = int(input("Enter your choice: "))
        if choice == 1:
            addTask()
        elif choice == 2:
            deleteTasks()
        elif choice == 3:
            viewTasks()
        elif choice == 4:
            print("Thanks for using to-do Application.\n")
            break
        else:
            print("Invalid input, please try again\n")


if __name__ == "__main__":
    main()