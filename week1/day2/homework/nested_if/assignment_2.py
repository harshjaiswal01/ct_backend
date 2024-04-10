# 2. Quick Decisions: The Event Planner 🎉
# Objective:

# To practice the use of shorthand if statements in determining event-related decisions.

# Task 1: Code Correction

# You are provided with a Python script that is supposed to help in event planning, but it has errors. Identify and fix them.

attendees = int(input("Enter number of attendees: "))

venue = "large hall" if attendees > 100 else "conference room"

print(venue)

# Task 2: Catering Choices

# Ask the user if they want "vegetarian" food. 
# Recommend "Veggie Delight Caterers" if yes, otherwise recommend "Gourmet Meals Caterers" using an inline if else statement.

food_choice = input("Would you like vegetarian food? Yes or No? ")

print("Veggie Delight Caterers" if food_choice == "Yes" else "Gourmet Meals Caterers")