
# 1. Tuple Mastery in Python
# Objective:
# The aim of this assignment is to deepen your understanding of tuples in Python, 
# along with their interaction with lists, dictionaries, and basic Python functionalities like functions, 
# input handling, and string formatting. By completing this assignment, you will enhance your skills in data structuring, 
# manipulation, and application of tuples in practical scenarios.

# Task 1: Formatting Flight Itineraries
# Create a Python function that takes a list of tuples as an argument. Each tuple contains information about a flight itinerary: 
# (traveler_name, origin, destination). The function should format and return a string that lists each itinerary. 
# For example, if the input is [("Alice", "New York", "London"), ("Bob", "Tokyo", "San Francisco")], the output should be a string formatted as:

# "Itinerary 1: Alice - From New York to London
#  Itinerary 2: Bob - From Tokyo to San Francisco"

def itinerary_assign(it_details):
    detailed_printout = ""
    i = 1
    for guest in it_details:
        name = guest[0]
        starting_location = guest[1]
        destination = guest[2]
        detailed_printout += "\nItinerary "+str(i)+" : "+str(name)+' - From '+str(starting_location)+ ' to '+ str(destination)
        i += 1
    return detailed_printout

itinerary = ("Alice", "New York", "London"), ("Bob", "Tokyo", "San Francisco")

answer = itinerary_assign(itinerary)
print(answer)