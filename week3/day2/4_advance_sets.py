#Advanced set methods

#used to compare 2 sets

#-- set1.issubset(set2) : returns True if all items from set1 can be found in set 2 else False

set1 = {1, 2,3,4}
set2 = {1, 2,3,4,5,6,7,8}

print(set1.issubset(set2)) #TRue

#-- set1.issuperset(set2) : returns True if set1 contains all items from set2 else True

print(set1.issuperset(set2)) #False because set1 doesnt contain all items of set2 #Inverse check of issubset()

#-- set1.isdisjoint(set2) : Checks for overlap. Returns TRUE if there are no common items between the sets

print(set1.isdisjoint(set2)) #False as there are common items

this_set = {'apple', 'banana', 'pear'}
veg_set = {'carrot', 'potato', 'brocolli'}

print(this_set.isdisjoint(veg_set)) #True because all values in both sets are different


