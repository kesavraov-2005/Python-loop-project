
#Question and project describtion.
'''Mini Project / Assignment Question
Project Title: Student Admission System
Problem Statement:
You are asked to create a Student Admission System for a school. The system should allow the user to:
1.	View all students currently admitted.
2.	Add a new student with roll number, name, class, and section.
o	If the student with the same roll number already exists, show a message: "Student already exists! Cannot add again."
3.	Search a student by roll number and display their details.
4.	Exit the system.
Requirements / Guidelines:
•	Use a dictionary to store student details with roll number as the key.
•	Use a loop to display the menu repeatedly until the user chooses to exit.
•	Use if-elif-else conditions to handle user choices.
•	For checking empty student list, use students == {}.
•	Display appropriate messages for successful addition, search results, or invalid inputs.
•	Keep the program simple and use only basic Python concepts: loops, conditionals, dictionaries, and strings.'''



#python code using loop
students = {
    "01": {"name": "kesav", "class": "10", "section": "A"},
    "02": {"name": "pavi", "class": "10", "section": "A"}}


while True:
    print("--- Student Admission Menu ---")
    print("1. Show Students")
    print("2. Add New Admission")
    print("3. Search Student")
    print("4. Exit")

    choice = int(input("Enter your choice : "))

    if choice == 1:
        if students == {}:
            print("No students admitted ")
        else:
            print("Current Students List:")
            for roll_no, details in students.items():
                print(f"Roll No: {roll_no}, Details: {details}")

    elif choice == 2:
        roll_no = int(input("Enter Roll No: "))
        if roll_no in students:
            print("Student already exists! Cannot add again.")
        else:
            name = input("Enter Name: ")
            stu_class = int(input("Enter Class: "))
            section = input("Enter Section: ")
            students[roll_no] = {"name": name, "class": stu_class, "section": section}
            print("New student added successfully!")

    elif choice == 3:
        if students == {}:
            print("No students in the system to search.")
        else:
            roll_no = input("Enter Roll No to Search: ")
            if roll_no in students:
                print(f"Found : {students[roll_no]}")
            else:
                print("Student not found!")

    elif choice == 4:
        print(" Thank you")
        break

    else:
        print("Invalid choice")       
            
