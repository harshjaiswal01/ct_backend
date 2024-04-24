#Set Operations

#merge sets 'specifically'

#-- set1.union(set2) : returns a set of all items from set1 and set2

set1 = {-1, 0, 1, 2,3,4}
set2 = {1, 2,3,4,5,6,7,8}

new_set = set1.union(set2) #It automatically removes duplicates and creates a new set. Doesnt update the original sets
print(new_set)

#-- set1.intersection(set2) : Return the overlaps between the sets : Returns a new set of all the common items

intersect = set1.intersection(set2)
print(set1.intersection(set2))
print(intersect)

#-- set1.difference(set2) : return all the items only from set1 that are different from the items in set2.

diff = set1.difference(set2)
print(diff)


#-- set1.symetric_difference(set2) : returns a set of all the non overlapping values from both sets

sym = set1.symmetric_difference(set2)
print(sym)

