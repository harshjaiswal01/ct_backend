#Set methods

#Membership checks on sets : check to see if item in set, return True or False
#One of the primary reason we use sets, because this happens instantaneously

my_set = {'superman', 'batman', 'wonder woomen', 'flash'}

print('spiderman' in my_set) #False
print('superman' in my_set) #True


#-- set.add(item) : add items to a set...works like apend
#If you try to add a duplicate item, it  simply gets ignored

my_set.add("green lantern")
print(my_set)

my_set.add("superman") #Nothing happens as he is already in there. No error.

#-- set.update(iterable) : will add all the items of that iterable (set, tuple, string, list, dict) to my set

marvel = ['iron man', 'thor', 'loki', 'dr. strange']
my_set.update(marvel)
print(my_set)

movies = {'End Game' : 'Avengers', "Far from Home":"Spider-Man", "Dark Knight" : "Batman"}

my_set.update(movies.keys()) #By default for Dictionary, Only adds the KEYS #.keys() for only keys, .values() for only values, .items() adds kvps as a tuple
print(my_set)

#-- set.remove(item) : removes an item from the set, will throw an error if the item does not exist in the set

my_set.remove('loki')
print(my_set)

# my_set.remove('thanos') #Will give KeyError as its not present

#-- set.discard(item) : removes an item from the set without throwing an error if the item doesnt exist

my_set.discard('green lantern')
print(my_set)

my_set.discard('green lantern') #No error this way!!!
print(my_set)

#-- set.pop() : removes a randon item from the set and returns it
#cant specify items

rand = my_set.pop()
print(rand)

print(my_set)


#-- set.clear() : removes all items

my_set.clear()
print(my_set)

