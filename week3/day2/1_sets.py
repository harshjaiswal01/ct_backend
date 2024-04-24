#Sets are a collection datatype in python, that can be immutable or mutable, unordered, unindexable and all
#items within a set must be unique and immutable

#Characteristics:
#-- Unordered : ITems in sets have no order and therefore cannot be indexed into
#-- Mutable : Basic sets are mutable. You can change how many items a set has and remove said items
#-- All elements in a set need to be unique, converting a list into a set will remove
#all duplicate items from the set
#-- All elements inside the set must be IMMUTABLE

#WHY BOTHER:
#-- ensures elements are unique
#-- instantaneous membership checks
#-- straight forward comparison operations

#Creating Sets

pop_set = {'one', 'two', 'three', ('this', 'that', 'other')}
print(pop_set)
print(type(pop_set))

empty_set = set() #{} will be empty dictionary. Use set()
print(type(empty_set))

alist = ['item', 'item', 'stuff', 'thing', 'oddity']
print(set(alist))
set_list = set(alist) #Converting list to set and remove all duplicates
alist = list(set_list) #Converting set to list
print(alist)

atuple = ('item', 'item', 'stuff', 'thing', 'oddity')
set_tup = set(atuple)
atuple = tuple(set_tup)
print(atuple)