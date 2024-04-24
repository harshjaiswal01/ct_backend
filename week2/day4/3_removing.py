# Removing items from a dictionary

dogs = {"Huge":"Great Danes", 'Large': 'German Shepard', 'Medium':"Pitt bull", "Shmedium" : "Pug", "Small":"Cocker Spaniel"}

#-- .pop(key) : remove the kvp associated with that key, return value

new_home = dogs.pop("Smll", "Not a Key/Category") #adding a second argument with a message to prevent KeyErrors when using bad keys
print(new_home)

new_home = dogs.pop("Small")
print(dogs)

#-- .popitem() : remove the last kvp (the one at the end)

dog = dogs.popitem() #returns a tuple with a key and value (k, v)
print(dog)
print(dogs)

#--- del dictionary[key] : deletes the kvp at that key

del dogs["Large"]
print(dogs)

#--- clear() : removes all kvps from the dictionary

dogs.clear()
print(dogs)

