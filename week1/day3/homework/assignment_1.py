# 1. Python List Transformation
# Objective: The aim of this assignment is to practice advanced list operations and transformations.

# Problem Statement: You've been given a list of numerical grades from a class exam. You need to process and analyze these grades.

# Task 1: Given the list of grades:

grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
# Sort the grades in descending order and display the sorted list.

grades.sort(reverse = True)
print(grades)



# Task 2: Calculate the average grade and display it.

sum_of_grades = sum(grades)
number_of_grades = len(grades)
average_grades = sum_of_grades / number_of_grades
print("Average grade of class is", average_grades)

# Task 3: Replace any grade below 80 with the value Failed.

grades[7] = "Failed"
grades[8] = "Failed"
grades[9] = "Failed"



print(grades)