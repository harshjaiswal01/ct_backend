#1. Decisions at the Crossroad

# Task 1: Code Correction
# You are provided with a Python script that uses conditional statements 
# to tell if a number is positive, negative, or zero, but it has some errors. Identify and fix them.

number = float(input("Enter a number: "))

if number > 0:
    print("The number is positive.")
elif number == 0:
    print("The number is zero.")
elif number < 0:
    print("The number is negative.")
else:
    pass
