# Task 1: Name Verification

# Problem Statement:  Write a function that takes in a list of names, 
# and verifies that the names are valid names using a regex pattern 
# and match(), and prints the name if it is valid, "Invalid name" if the name is not.

# Use the following list as an argument to test your function.

# Code Example:
import re

names = ["Abraham Lincoln", "Andrew P Garfield", "peter pan", 
         "Connor Milliken", "Jordan Alexander Williams", 
         "Madonna", "programming is cool"]


# names1 = re.split(r', ', names)

def name_verification(name_list):
    for name in name_list:
        name_match = re.match(r"[A-Z]\w*\s[A-Z]*\w*\s*[A-Z]\w*", name)
        if name_match:
            print(name_match.group())
        else:
            print('Invalid Name')

name_verification(names)

