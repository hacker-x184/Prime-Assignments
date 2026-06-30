students = {}
while True:
    choice = input("A - Add a student\nB - Update marks\nC - Search for a student\nD - Display all students and marks\nE-To close the program\nEnter choice (A/B/C/D/E): ").upper()

    if choice == "A":
        name = input("Enter student name: ").lower()
        marks = int(input("Enter marks: "))
        students[name] = marks
        print("Student added successfully!")

    elif choice == "B":
        name = input("Enter student name: ")

        if name in students:
            marks = int(input("Enter new marks: "))
            students[name] = marks
            print("Marks updated successfully!")
        else:
            print("Student not found!")

    elif choice == "C":
        name = input("Enter student name: ")

        if name in students:
            print("Marks:", students[name])
        else:
            print("Student not found!")

    elif choice == "D":
        if len(students) == 0:
            print("No students found!")
        else:
            for name, marks in students.items():
                print(name, ":", marks)
    elif choice == "E":
        break
    else:
        print("Invalid choice!")