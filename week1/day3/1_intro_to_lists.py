#List in python are collections of items and are mutable, ordered and have dynamic sizing
#lists are another datatype in python

#-- ordered: each item has a position which allows me to know where each item is
#-- lists are mutateble which means the ability to mutate lists...add, remove and manipulate
#-- dynamic size: add and remove from list allowing them to grow and shrink

#lists are created with square brackets [] and each item is seperated by ','

#empty list

empty_list = []

#populated list

people = ['Bob', 'Barry', 'Bernie', 'Bill']

#python list can hold a veriety of different

stuff = [12, 'apple', False, 3.14, ['Dylan', 'Travis']]

#another thing we can have duplicate items in list

toppings = ['pepperoni', 'pepperoni', 'pepperoni']

#-- LIST INDEX

#each item has a position marked by an index
#indices are in numeric order starting from 0
#and remove items from our list

#indices     0        1       2         3
alist = ['item1', 'item2', 'item3', 'item4']
print(alist)

#grabbing item3

print("third item", alist[2])

#List within a list
print(stuff[4][0])

#grabbing the last item with idx -1
print('last item', alist[-1])

#potential pitfalls

#Indexerror
#-- index out of range, trying to access an index that doesnt exist

#print(alist[4])