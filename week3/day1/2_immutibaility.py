#Immutability means that the data of a tuple cannot be adjusted in its location in memory

tup1 = (1, 2, 3, 4, 5)
print(tup1)

# tup1[3] = 6 #Will Throw a TypeError since tuples cant do this

#YOU CANNOT CHANGE TUPLE DATA IN PLACE

#-- Small work around to change item in a tuple
#convert the tuple into a list, make changes and convert back to tuple

tup1 = list(tup1)
print(tup1)
tup1[3] = 'four'
tup1 = tuple(tup1)
print(tup1)

#-- concatenating tuples : adding them together

tup1 = 1,2,3,4,5
tup2 = 6,7,8,9,10
tup1 += tup2
print(tup1)

#-- repeating tuples
short_story = 'A tale',
print(short_story)
anthology = short_story * 3
print(anthology)