"""
Problem:
Write a Python program to calculate the results of 5 students.
For each student, input their name and marks in English, Maths, and Science.
Display the total marks, average marks, percentage, and result.

Assumption: Each subject is marked out of 100. A student passes when
their marks are at least 40 in every subject.
"""

NUMBER_OF_STUDENTS = 5
SUBJECTS = ("English", "Maths", "Science")


for student_number in range(1, NUMBER_OF_STUDENTS + 1):
    print(f"\nStudent {student_number}")
    name = input("Enter student name: ")
    marks = []

    for subject in SUBJECTS:
        mark = float(input(f"Enter marks in {subject}: "))
        marks.append(mark)

    total = sum(marks)
    average = total / len(SUBJECTS)
    percentage = (total / (len(SUBJECTS) * 100)) * 100
    result = "Pass" if all(mark >= 40 for mark in marks) else "Fail"

    print(f"\nResult for {name}")
    print(f"Total marks: {total:.2f} / {len(SUBJECTS) * 100}")
    print(f"Average marks: {average:.2f}")
    print(f"Percentage: {percentage:.2f}%")
    print(f"Result: {result}")