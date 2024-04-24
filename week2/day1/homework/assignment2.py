# 2. The Shopping List Maker
# Objective: The aim of this assignment is to create a program that helps users make a shopping list.

# Task 1: Write a function that lets the user add items to a list until the user replies "stop", and then returns the shopping list. 
# Task 2: Include a feature to remove items from the list. 

list_a = []

def shop_add(a):
    list_a.append(a)

def shop_delete(a):
    list_a.remove(a)

i = 0

while i == 0:

    b = input("Would you like to add or remove items to your shopping list? Please enter A to Add or B to Remove or C if your finished: ")

    if b == "A":
        shop_add(input("Please enter the item name: "))
    elif b == "B":
        shop_delete(input("Please enter the item to delete: "))
    elif b == "C":
        i = 1

# Task 3: Add a feature that prints out the entire list in a formatted way.

j = 1

print("Here is your Shopping list:-")

for items in list_a:
    print(f"{j}. ", items)
    j += 1
