#Math Operations

#Order Operations
#(3+4)+4^2-6*5
#PEMDAS
# First Paranthesis(Brackets)
# Then Exponents
# Then Multiplation and Divide tied (left to right priority)
# Then Addition
# Then Subtraction

order_op = (3+4)+4**2-6*5
print("Order OP Test", order_op)

#Addition use +

my_sum = 3 + 4 + 5
print(my_sum)

#Addition assign: reassign the variable to its current value plus a new value

my_sum += 2 #my_sum = my_sum + 2
print(my_sum)

#Subtraction use '-'

my_diff = 100 - 10
print(my_diff)

#Subtract assign

my_diff -= 1
print(my_diff)

#Multiplication use = "*"

mul = 8 * 8
print(mul)

#Multiply assign

mul *= 2
print(mul)

#Division using "/"
#Division always returns float
#If you incorporate a float in any other math operation, it will convert it to float

quotient = 10 / 2
print(quotient)

#Division Assign

quotient /= 2
print(quotient)

# Floor Division use '//' (Rounds down to the nearest whole number)

pre_rounded = 10/7
print (pre_rounded)

rounded = 10//7
print(rounded)

#Floor Divide Assign
x = 40
x //= 2

print(x)

#Module use '%' returns the remainder of division
remainder = 15 % 6
print(remainder)

#Module Assign
remainder %= 3
print("Module assign", remainder)

#Exponents use "**"
square = 11**2
print(square)

cubing = 11**3
print(cubing)

#exponent Assign

square **=2
print(square)

