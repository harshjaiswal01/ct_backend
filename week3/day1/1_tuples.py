#They are immutable : Cannot be changed in the memory
#Tuples are a datatype similar to a list with the exception that they are immutable

#Characteristics:
#-- Immutable : YOu cannot edit the data of a tuple with having to reassign it.
#-- ORdered : Like lists they have an order, and you can access the elements by index
#-- Like lists, they can store a variety of objects including duplicate objects

#Why bother:

#Create a collection that will not be changed by you or another dev

#Iterating over a tuple is faster than iterating over a list.

#creating Tuple
#we use () to define tuples
empty_tup = () #empty no items

#sindleton, tuple with one item

singleton = ('element',) #requires a trailing comma

print(singleton)
print(type(singleton))

#multi-element tuple : dont need a trailing comma

pop_tup = ('this', 'is', 'a', 'populated', 'tuple')
print(pop_tup)

variety_tup = (4, 'Five', 6.0, [7,8,9], {"ten":10, "nine": 9}, True, False, False) #can store just about anything and duplicates
print(variety_tup[4]["nine"])

#packing tuples : without brackets

packed = "t-shirt", "pants", "Jacket", "Shoes"
print(packed)

tup_pack = pop_tup, variety_tup, packed
print(tup_pack)
print(tup_pack[1][3][1]) #Grabbing 8 from variety tup in tup pack

#slicing [start:stop] : Default start = 0 and stop = end of the tuple
#Stop is not included

duple = (True, True, True, False, False, False)
print(duple[:3]) #Grabbing all True's #Returning a sub-tuple from 0 to 3

#Inclass Indexing

historical_record = ("Medieval Era", ("Knights", "Castles", ("King", "Queen")), "Renaissance Period")
print(historical_record[1][2][1]) #Grabbing Queen









