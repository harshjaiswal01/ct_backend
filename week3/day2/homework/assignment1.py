# 1. Python Sets Adventure
# Objective:
# The aim of this assignment is to deepen your understanding and application of Python sets in 
# various scenarios, ranging from basic operations to advanced manipulations and best practices. 
# You will correct given codes, use sets in everyday contexts, and tackle challenges that require creative thinking and problem-solving.

# Task 1: Flight Route Comparison
# Imagine you work for an airline and need to compare the flight routes of your airline with a competitor. 
# You have two sets of flight destinations, one for each airline. Write a Python program to find out:

# Destinations that both airlines fly to.
# Destinations unique to your airline.
# Whether there are any destinations that neither airline shares.
# Example Code:

our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}

def both_airline(set1, set2):
    common_destinations = set1.intersection(set2)
    print(f"\nCommon Destinations served by both airlines are {common_destinations}")

def unique_destinations(set1, set2):
    our_unique = set1.difference(set2)
    competitor_unique = set2.difference(set1)
    print(f"\nUnique destinations served by our airline are {our_unique}")

def neither_airline(set1, set2):
    neither = set1.symmetric_difference(set2)
    print(f"\nDestinations that neither airlines share are {neither}")

both_airline(our_routes, competitor_routes)
unique_destinations(our_routes, competitor_routes)
neither_airline(our_routes, competitor_routes)