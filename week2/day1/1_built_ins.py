#Python built in functions

#-- print(value) : prints this value to your terminal
#One of the most important tools in debugging and viewing stared values

print('Hello there')
var = 'A value inside this var'
print(var)

#String COncatenation : adding string together

word1 = 'Hello'
word2 = 'World'
word3 = word1+word2
print(word3)

word4 = word1 + ' ' + word2
print(word4)

#String formatting : embedding variables directly into a string

#--f string

attribute = 'Spicy'
fav_food = 'Tacos'
statement = f'Hi, my fav food is {attribute} {fav_food}'
print(statement)

#-- .format()

age = 99
statement = 'Hi, I am {} years old'.format(age)
print(statement)

#-- input() : Allows us to retrieve user imput and return it as a string

#Uncomment the following to see how

dog_name = input("What is your dogs name? ")
# print(f'Wow I love the name {dog_name}!')

# age = input("How old are you? ")
# birthday = int(age) + 1
# print(f'On your birthday, you will be {birthday} years old!')

#-- type() : returns the datatype of the particular value

var1 = True
var2 = 'Words'
var3 = 5
var4 = 5.5
var5 = ['item', 'item', 'item']

print(type(var1))
print(type(var2))
print(type(var3))
print(type(var4))
print(type(var5))

#-- len() : returns the length of an iterable as an int

print(len(var5))

name = 'Dylan'
print(len(name))

#-- isinstance(var, type) return True of False depending on if the var is that type
#types str, int, float, bool, list

var = 'Hi there'
num = 4
print(isinstance(var, list))
print(isinstance(var, str))
print(isinstance(num, float))
print(isinstance(num, int))

forecast = ['Monday', 84.2, 'Teusday', 78.9, 'Wednesday', 82.1]

total = 0
i = 0

for item in forecast:
    if isinstance(item, float):
        total = total+item
        i += 1

average = total / i
print(average)
print(total / 3)

#-- abs() : returns the absolute value of a number (The positive value)

x = 6
y = -3
print(abs(x))
print(abs(y))

#-- round() : rounds any float to the nearest whole number, returns an int. .5  and down rounds down

a = 4.7
print(round(a))

#-- sum(list) : returns the total sum of a list of numbers

nums = [1, 2, 3, 4, 5]
total = sum(nums)
print(total)

#-- min(list) : returns the minimum value of a list of numbers

minimum = min(nums)
print(minimum)

#-- max(list) : returns the max value of a list of numbers
maximum = max(nums)
print(maximum)

#-- pow(num, exp) : raises a number to the power of exp passed, substitute for **

print(pow(4, 2))

#-- divmod(num, divisor) : returns a tuple, quotient and the remainder

print(divmod(8, 2))
print(divmod(9, 2))

tup = divmod(8, 5)
print(tup)
print(tup[0]) #to get the value


