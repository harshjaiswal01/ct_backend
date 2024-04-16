# 1. The Calculator App
# Objective:
# The aim of this assignment is to build a basic calculator that can perform addition, subtraction, multiplication, and division.

# Task 1: Create functions for each arithmetic operation.
    
print("Assignment 1, Task 1")

def add(a, b):
    return a + b

def subt(a, b):
    return a - b

def mult(a, b):
    return a * b

def divide(a, b):
    if(b == 0):
        return ("not possible as Division by Zero is not possible")
    else:
        return a / b
    
# Task 2: Implement user input to receive numbers and an operation choice.
# Task 3: Ensure your program can handle division by zero and other potential errors.

i = 0

while i == 0:
    
    op = input("Would you like to A. Add, B.Subtract, C.Multiply or D.Divide? Please answer in A, B, C or D? ")

    a = float(input("Please enter the first number: "))
    b = float(input("Please enter the second number(or Divisor for division): "))

    if op == 'A':
        print(f"The sum of {a} and {b} is", add(a,b))
    elif op == 'B':
        print(f"{a} minus {b} is equal to", subt(a, b))
    elif op == "C":
        print(f"{a} multiplied by {b} is", mult(a, b))
    elif op == "D":
        print(f"{a} divided by {b} is", divide(a, b))

    j = input("Would you like to try again? Yes or No? ")
    if j == "No":
        i = i + 1



