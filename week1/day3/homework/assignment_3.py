# 3. Deep Dive into Python Lists
# Objective: The aim of this assignment is to integrate various list operations and methods to solve a complex problem.

# Problem Statement: You're organizing a school event, and you have lists containing student names, their grades, and the activities they're interested in.

# Task 1: Given the lists:

students = ["John", 'Doe', 'Jane', 'Smith']
grades = [85, 90, 78, 88]
activities = ['Football', 'Music', 'Art', 'Dance']

# Print the name, grade and activiy of students with a score below 80. Expected Outcome "Jane", 78, "Art"
i = 0

while i < 4:
    if grades[i] < 80:
        print("Student Details with less that 80:", students[i],",", grades[i],",", activities[i])
        j = i
    i = i+1

# Task 2: For the remaining students, 
# grab their name directly from  the students list name in a new list named students_approved. 
# Expected Outcome: students_approved = ["John", "Doe", "Smith"]


students.pop(j)
grades.pop(j)
activities.pop(j)

students_approved = students.copy()

# Task 3: Print the list students_approved

print(students_approved)