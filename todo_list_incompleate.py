todo_list = ["Math homework", "Science project", "Read history book", "Practice piano"]

def display_todo_list():
    print(f"To do list :\n")
    for i in todo_list:
        print (i)

def add_task(): 
    print("What task would you like to add?")
    todo_list.append(input())
    display_todo_list()

def remove_task():
    task = input("What task would you like to remove?")
    if task in todo_list:
        todo_list.remove(task)
        display_todo_list()
    else:
        print("ERROR Task not found")
        display_todo_list()

def find_task():
    task = input("What task would you like to find?")
    if task in todo_list:
       print(todo_list.index(task))
    else:
        print("Task not found")
       

def complete_task(): 
    del todo_list[0]
    print("Task complete")
    display_todo_list()

def filter_tasks(keyword):
    filtered_tasks = [task for task in todo_list if keyword in task]
    print(filtered_tasks)
    print(f"\nTasks containing '{keyword}':")
    print(filtered_tasks if filtered_tasks else "No tasks found.")


def main():
    while True:
        print("\nTo-Do List Manager Menu")
        print("1. View To-Do List")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Find Task")
        print("5. Complete First Task")
        print("6. Filter Tasks by Keyword")
        print("7. Exit")
        
        choice = input("\nEnter your choice: ")
        if choice == "1":
            display_todo_list()
        if choice == "2":
            add_task()
        if choice == "3":
            remove_task()
        if choice == "4":
            find_task()
        if choice == "5":
            complete_task()
        if choice == "6":
            keyword = input("Insert keyword of the task you are looking for: ")
            filter_tasks(keyword)
        if choice == "7":
            break

main()