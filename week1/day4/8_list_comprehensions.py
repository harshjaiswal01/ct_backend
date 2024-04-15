#list comprehensions are inline for loops that product a list

#syntax

# var = [<added item> for item in iterable]

students = ['Ed', 'edd', 'eddy']

shirt_list = ['Shirt' for student in students]
print(shirt_list)

#List comp with if statement

# var = [<added item> for item in iterable if condition]

nums = [1,2,3,4,5,6,7,8]

evens = [num for num in nums if num % 2 == 0]
print(evens)

#list comp with 'if' and 'else'

#Syntax

# var = [<if true add> if (condition) else <else add> for item in iterable]

grades = [100, 98, 52, 87, 98, 68]

pass_fail = ['pass' if grade>=70 else 'fail' for grade in grades]

print(grades)
print(pass_fail)

