# task1.py
# Student Management System with File Storage

# Function to calculate grade based on average marks
def calculate_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 80:
        return "B"
    elif avg >= 70:
        return "C"
    elif avg >= 60:
        return "D"
    else:
        return "Fail"

# Function to add a new student
def add_student():
    name = input("Enter Student Name: ")
    roll_no = input("Enter Roll No: ")
    marks1 = int(input("Enter marks of Subject 1: "))
    marks2 = int(input("Enter marks of Subject 2: "))
    marks3 = int(input("Enter marks of Subject 3: "))

    avg = (marks1 + marks2 + marks3) / 3
    grade = calculate_grade(avg)

    student = {
        "Name": name,
        "RollNo": roll_no,
        "Marks": [marks1, marks2, marks3],
        "Average": avg,
        "Grade": grade
    }

    # Save student record into a file
    with open("students.txt", "a") as f:
        f.write(str(student) + "\n")

    print(" Student added successfully!\n")

# Function to view all students
def view_students():
    try:
        with open("students.txt", "r") as f:
            lines = f.readlines()
            for line in lines:
                student = eval(line.strip())  # Convert string back to dictionary
                print(student)
    except FileNotFoundError:
        print(" No records found. Please add students first.\n")

# Function to search student by Roll No
def search_student():
    roll_no = input("Enter Roll No to search: ")
    found = False

    try:
        with open("students.txt", "r") as f:
            lines = f.readlines()
            for line in lines:
                student = eval(line.strip())
                if student["RollNo"] == roll_no:
                    print(" Student Found:", student)
                    found = True
                    break
        if not found:
            print(" Student not found.\n")
    except FileNotFoundError:
        print(" No records found.\n")

# Main Menu
while True:
    print("\n--- Student Management System ---")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student by Roll No")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        print(" Exiting... Goodbye!")
        break
    else:
        print(" Invalid choice. Try again.\n")
