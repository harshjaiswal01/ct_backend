# 2. The Greatest Showdown
# Objective: Harness the power of conditional statements to compare and determine values.

# Task 1: Identify the Greatest Write a Python program that prompts the user to enter three numbers. 
# The program should then identify and print out the largest number among the three.

number1 = int(input("Please enter the first number: "))
number2 = int(input("Please enter the second number: "))
number3 = int(input("Please enter the third number: "))

greatest = ""

if number1 > number2 and number1 > number3:
    greatest = number1
elif number2 > number3 and number2 > number3:
    greatest = number2
elif number3 > number1 and number3 > number2:
    greatest = number3

print("The greatest number is", greatest)


# Task 2: Identify the Smallest also determine the smallest number among the three and print it out. 
# (For bonus points create a continuous if elif else chain that extends from task 1 and will identify both largest and smallest numbers)

smallest = ""

if number1 < number2 and number1 < number3:
    smallest = number1
elif number2 < number3 and number2 < number3:
    smallest = number2
elif number3 < number1 and number3 < number2:
    smallest = number3

print("The smallest number is", smallest)

print("The largest number is", greatest, "and the smallest number is", smallest)