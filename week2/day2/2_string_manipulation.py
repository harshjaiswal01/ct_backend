#String Concatenation : adding two or more strings together using +

word_1 = 'Big'
word_2 = 'Apple'

new_york = word_1 + ' ' + word_2 #Dont forget space
print(new_york)

#repeat strings by multiplying with *

chant = "LETS GO TEAM! "
full_chant = chant*3
print(full_chant)

#Addition assign
#adds new value to current value and re-assigns variable to combination

word = 'Hello'
print(id(word))
word += " there"
print(word)
print(id(word))

#Multiply Assign
#Allows you to repeat a string x amount of times

repeat_i = 'I'
repeat_i*= 5
print(repeat_i)
