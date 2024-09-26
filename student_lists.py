students=["Aria", "Mason", "Harper", "Jackson", "Lily", "Stella", "Jasper", "Scarlett", "Ruby", "Aiden"]
def display_students():
    print(f"Current students:\n")
    for i in students:
        print(i)
    
def add_student():
    print("Would you like to add a new name? If so insert the name" )
    students.append(input())
    display_students()

def remove_student():
    name = input("What name would you like to remove?(insert name)")
    if name in students:
        students.remove(name)
        display_students()
    else:
        print("ERROR Name not found")

def pop_student():
    if len(students) == 0:
        print("Error no names found")
    else:
        remove_student =students.pop()
        print(f"Student removed:{remove_student}")
        display_students()

def update_student():
    name_update = input("What is the current name of the student?")
    if name_update in students:
        index = students.index(name_update)
        new_name = input("New name: ")
        students[index] = new_name
        display_students
    else:
        print("There is no student with that name on the list")
        
def menu():
   while True:
    print("\nMenu:")
    print("1. Add a student")
    print("2. Remove a student")
    print("3. Pop a student")
    print("4. Update a student's name")
    print("5. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        add_student()
    if choice == "2":
        remove_student()
    if choice == "3":
        pop_student()
    if choice == "4":
        update_student()
    if choice == "5":
        break
    
menu()
