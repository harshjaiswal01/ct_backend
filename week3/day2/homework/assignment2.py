# 2. Set Operations in Data Analysis
# Objective: The aim of this assignment is to enhance your skills in using Python sets for data analysis tasks. 
# You will apply various set operations to handle real-world data scenarios, focusing on their practical application and efficiency.

# Task 1: Duplicate Entries Cleanup You are given a list of customer IDs, some of which are duplicated. 
# Write a Python function that takes in a list of customer ID's, removes duplicates, prints each unique id, and returns a set of the unique IDs

# Example Code:

customer_ids = ["C001", "C002", "C003", "C002", "C001", "C004"]

def remove_dup(data_set):
    new_set = set(data_set)
    new_list = list(new_set)
    print("\nPrinting Each Unique Id:-")
    for stuff in new_list:
        print(stuff)
    return(new_list)

print("\nThe complete new set of Unique ID's:-")
new_list = remove_dup(customer_ids)
print(new_list)
    