# The show_menu function welcomes the user and prints the options the user can choose from to continue in the program
def show_menu():
    print("Welcome to the students record program!")
    print("What would you like to do today?")
    print("1 - Find a student?")
    print("2 - Edit a student's info using student ID?")
    print("3 - Add a new student?")
    print("4 - Remove a student?")
    user_choice = input("Please enter your choice:\n")
    return user_choice
    
# add is a list that has keys that correspond to the users input that stores the inputs into "students" by using append
def add(students, sid, name, gpa, semester):
    students.append({"id": sid, "name": name, "gpa": gpa, "semester": semester})
    print("Student added")
 
# remove is used when the user wants to remove a student from the list by entering an id that was added to the list previously
def remove(students, sid):
    for student in students:
        if student["id"] == sid:
            students.remove(student)
            print("Student removed")
            return
    print("Student not found")
 
# edit_name is a function that lets the user change a students name that they have previously entered
# by entering their id and then inputing a new name
def edit_name(students, sid, new_name):
    for student in students:
        if student["id"] == sid:
            student["name"] = new_name
            print(f"Student name modified for the student with id {sid}")
            print(f"Student's new name is {new_name}")
            return
    print("Student not found")
 
# search goes through the "students" list and uses the id inputed to find a student who correspondes to that id
# if the student is found it prints the student and their other info. If not found it says "student not found"
def search(students, sid):
    for student in students:
        if student["id"] == sid:
            print("Student found")
            print(f"{student['id']}\t{student['name']}\t{student['gpa']}\t{student['semester']}")
            return
    print("Student not found")
 
# run_add lets the user add a student into the list (their id, name, gpa, and semester)
# it adds the info and stores it into the students list and matches them with the keys
# it also lets the user decide if they want to keep adding more students or not
def run_add(students):
    while True:
        print("Enter id of the student, followed by the student's information.")
        sid = input("id: ")
        name = input("name: ")
        gpa = input("gpa: ")
        semester = input("semester: ")
        add(students, sid, name, gpa, semester)
        print(f"{sid}\t{name}\t{gpa}\t{semester}")
        again = input("Do you want to add a new student? y(yes)/n(no): ").lower()
        if again not in ['y', 'yes']:
            break
 
# run_search lets the user search for a student in the list by their id until they enter -1
def run_search(students):
    while True:
        sid = input("Enter the id of the student. Enter -1 to return to the previous menu: ")
        if sid == "-1":
            break
        search(students, sid)
 
# run_edit lets the user edit students name in the list until -1 is entered
def run_edit(students):
    while True:
        sid = input("Enter the id of the student. Enter -1 to return to the previous menu: ")
        if sid == "-1":
            break
        new_name = input("Enter the new name of the student: ")
        edit_name(students, sid, new_name)
 
# run_remove lets the uer remove students from the list until they enter -1
def run_remove(students):
    while True:
        sid = input("Enter id of the student that you want to remove from the students' registry. Enter -1 to return: ")
        if sid == "-1":
            break
        remove(students, sid)
        again = input("Do you want to remove more students? y(yes)/n(no): ").lower()
        if again not in ['y', 'yes']:
            break