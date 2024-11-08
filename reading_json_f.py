import json
def load_data(filename):
    students={}
    with open(filename, "r") as file:
        reader = json.load(file)
        for student_id,student_info in reader.items():
         student = student_info[0]
         name = student["name"]
         grade = student["grade"]
         group = student["group"]
         
         students[student_id]= [name, grade, group]
    return students

def main():
    students = load_data("data.json")
    for student_id, student_info, in students.items():
        print(f"Student_ID: {student_id}")
        print(f"Name: {student_info[0]}")
        print(f"Grade:{student_id[1]}")
        print(f"Group:{student_info[2]}")
        print()
        

main()