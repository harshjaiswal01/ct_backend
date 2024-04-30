# Task
# Given the a list of numbers, return a fixed list so that the values increment by 1 for each index from the minimum value up to the maximum value (both included).

# Example
# Input:  1,3,5,6,7,8 Output: 1,2,3,4,5,6,7,8

# input_list1 = [1,2,9]

def solution(input_list):
    max_value = max(input_list)
    min_value = min(input_list)
    new_list = []
    i = min_value
    while i <= max_value:
        new_list.append(i)
        i += 1
    return new_list

# print(solution(input_list1))
