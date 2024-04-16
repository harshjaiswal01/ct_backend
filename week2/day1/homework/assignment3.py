# 3. The Grade Analyzer
# Objective: The aim of this assignment is to analyze a set of grades and provide statistics.

# Task 1: Code a function to calculate the average grade. 



def average_grade(grades):
    i = 0
    sum_of_grades = 0
    for grade in grades:
        sum_of_grades = sum_of_grades + int(grade)
        i += 1
    j = sum_of_grades / i
    return j


grade_list = []

i = 0
while i == 0:
    j = int(input("Please enter the grade of Student or enter 0 if you are done: "))
    if j == 0:
        break
    else:
        grade_list.append(j)

print('''
      
      ''')

print("The average grade of", len(grade_list), "Students in class is:", average_grade(grade_list))

print('''
      
      ''')

# Task 2: Implement a function to find the highest and lowest grade. 
highest = 0
lowest = grade_list[0]

for grade in grade_list:
    a = grade
    if a >= highest:
        highest = a
    elif a <= lowest:
        lowest = a

print(f"The highest grade in the class of {len(grade_list)} is {highest} and the lowest is {lowest}")

alphabetical_grades = []

print('''
      
      ''')


# Task 3 (BONUS): Create a feature that categorizes grades into letter grades (A, B, C, etc.).

for grade in grade_list:
    if grade >= 90:
        alphabetical_grades.append("A")
    elif grade >= 80 and grade < 90:
        alphabetical_grades.append("B")
    elif grade >= 70 and grade < 80:
        alphabetical_grades.append("C")
    elif grade >= 60 and grade < 70:
        alphabetical_grades.append("D")
    else:
        alphabetical_grades.append("F")

# print(alphabetical_grades)
print("The following are the grades and their corresponding letter grades:")
i = 0
c = 1
for grade in grade_list:
    print(f"{c}. {grade} : {alphabetical_grades[i]}")
    i += 1
    c += 1
