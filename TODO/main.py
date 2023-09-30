TASK_FILE = 'todo.txt'

def show_menu():
    print('\n')
    print('==========Welcome to your todo list==========')
    print('1. View task')
    print('2. add task')
    print('3. Delete task')
    print("4. Edit task")
    print("5. Enter task as completed")
    print('6. Exit')

def view_task():
    try:
        with open(TASK_FILE, 'r') as file:
            f = file.readlines()
            
            if not f:
                print('You have no tasks to view. Please add tasks to view')
            else:
                for index, task in enumerate(f, start=1):
                    print(f"{index}. {task.strip()}")
    except FileNotFoundError:
        print('You have no tasks to view. Please add tasks to view')

def add_task():
    add = input("Enter Task: ")
    with open(TASK_FILE, "a") as file:
        file.write(add + "\n")
    with open(TASK_FILE, 'r') as file:
            print('Task added successfully')

def del_task():
    view_task()
    task_number = int(input("Enter the task number to delete: "))
    with open(TASK_FILE, "r") as file:
        lines = file.readlines()
    if task_number <= len(lines):
        deleted_task = lines.pop(task_number - 1).strip()
        with open(TASK_FILE, "w") as file:
            file.writelines(lines)
        print(f"Task '{deleted_task}' deleted successfully!")
    else:
        print("Invalid task number.")

def edit_tasks():
    try:
        with open(TASK_FILE, 'r') as file:
            tasks = file.readlines()

        if not tasks:
            print("Please add tasks")
            return

        view_task()
        task_number = int(input("Enter what task would you like to edit: "))

        if task_number <= len(tasks):
            index_to_edit = task_number - 1

            edited_task = input("Enter the edited task: ")
            tasks[index_to_edit] = edited_task + "\n"
            
            with open(TASK_FILE, "w") as file:
                file.writelines(tasks)

            print(f"Task '{edited_task}' edited successfully")
        else:
            print("You have entered an invalid task number")

    except FileNotFoundError:
        print('You have no tasks to edit. Please add tasks first.')

def completed_task():
        
    with open(TASK_FILE, "r") as file:
        tasks = file.readlines()

    view_task()

    task_number_to_complete = int(input("Enter the designated task number to mark as completed: "))

    if 1 <= task_number_to_complete <= len(tasks):
        completed_task = tasks[task_number_to_complete - 1].strip()
        completed_task += " (completed\n)"
        tasks[task_number_to_complete - 1] = completed_task

        with open(TASK_FILE, 'w') as file:
            file.writelines(tasks)
            print(f"Task '{completed_task.strip()} marked as completed")
    else:
        print("Invalid task number")

def main():
    while True:
        show_menu()
        request = input('What service would you like: ')
        if request == '1':
            view_task()
        if request == '2':
            add_task()
        if request == '3':
            del_task()
        if request == '4':
            edit_tasks()
        if request == '5':
            completed_task()
        if request == '6':
            break
if __name__ == "__main__":
    main()
