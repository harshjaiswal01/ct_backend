#Task 1: Validating Calculations Calculate the value of a particular arithmetic expression twice: once normally, 
# and once using parentheses. Compare the two results to see if they match.

a = 10
b = 13
c = 15
d = 12
e = 100
f = 25
g = 40
h = 2
first_try = a*b + c-d + e / f + g / h
print("First try", first_try)

second_try = (a*b) + (c-d) + (e / f) + (g / h)
print("Second Try", second_try)

third_try = g / h + a*b + c + e / f - d
print("Third Try", third_try)
