# Given an array of integers.

# Return an array, where the first element is the count of positives numbers 
# and the second element is sum of negative numbers. 0 is neither positive nor negative.

# If the input is an empty array or is null, return an empty array.

# Example
# For input [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15], you should return [10, -65].

#1. We are going to traverse the list and count positives
#2. Then we are going to traverse for negatives and add the sum of negatives
#3. REturn the answer and print

def solution(array1):
    i = 0 #Count of Positives
    sum_negative = 0 #Sum of Negatives
    for numbers in array1:
        if numbers > 0:
            i += 1
        elif numbers < 0:
            sum_negative += numbers
    if array1 == []:
        return []
    else:
        return [i, sum_negative]