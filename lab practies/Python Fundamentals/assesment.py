# Grade Management System

# List to store student records
students = []

# Function to calculate grade
def calculate_grade(marks):
    if marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 50:
        return "D"
    else:
        return "Fail"

# Function to add a new student
def add_student():
    name = input("Enter student name: ")
    marks = float(input("Enter marks out of 100: "))
    grade = calculate_grade(marks)
    students.append({"name": name, "marks": marks, "grade": grade})
    print(f"Student {name} added successfully with grade: {grade}\n")

# Function to display all student records
def display_students():
    if not students:
        print("No student records found.\n")
        return
    print("\n--- Student Records ---")
    for student in students:
        print(f"Name: {student['name']}, Marks: {student['marks']}, Grade: {student['grade']}")
    print()

# Main menu loop
def main():
    while True:
        print("Grade Management System")
        print("1. Add Student")
        print("2. Display All Students")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            add_student()
        elif choice == '2':
            display_students()
        elif choice == '3':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

# Run the program
main()
