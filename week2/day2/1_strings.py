#Strings are out datatype for storing text

astring = 'this is a string with \' single \'quotes'
bstring = "this is a string with double quotes"

#-- They are Immutable
#-- This means you cant change the data is stored in memory
#-- You can however still reassign

word = "Hello"
print(word)
print(id(word))

#Whenever we try to manipulate a string, we simply add the modifications and move them to a new slot in memory

#Indexing into strings

name = "Kevin"
second_letter = name[1]
print(second_letter)

#Slicing in strings
#Same as slicing list [start:stop] stop is non-inclusive

pie = 'apple pie'
apple = pie[:5]
print(apple)

pie = pie[6:]
print(pie)

#reverse slice
palindrome = "tacos are cool"
reversed = palindrome[::-1]
print(reversed)

