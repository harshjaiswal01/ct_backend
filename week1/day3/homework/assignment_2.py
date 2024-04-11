# 2. Advanced Slicing Techniques
# Objective: The aim of this assignment is to master the art of slicing in Python lists.

# Problem Statement: You have a list of daily temperatures for a month, and you'd like to extract specific data from it.

# Task 1: Given the list of temperatures:

temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]

#Extract Temps for Second Week

second_week_temperatures = temperatures[7:14]
print("Second Week Temps:", second_week_temperatures)

#Task 2: Extract all temperatures above 100

temp_above_100 = temperatures[23:]

print("All Temps above 100:", temp_above_100)

temperatures.reverse()

reverse_temp_5_to_10 = temperatures[4:10]
print("Reverse Temp from Day 5 - Day 10 :", reverse_temp_5_to_10)
