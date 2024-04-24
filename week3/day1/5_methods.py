#Tuples dont have too many methods

#-- tuple.count(item) : counts how many times an item appears in a tuple

shopping = 'egg', 'milk', 'creamer', 'creamer', 'creamer', 'creamer', 'chicken'

print(shopping.count('creamer'))

#-- len(tuple) : gives the count of index in tuple

print(len(shopping))

#-- tuple.index(item) : returns the first index of the item

print(shopping.index("chicken"))
print(shopping.index("creamer"))

#-- Membership checks of a tuple, if item in tuple, 'in', Returns True or False depending

print('creamer' in shopping) #Returns true or false
print('cinnamon' in shopping)