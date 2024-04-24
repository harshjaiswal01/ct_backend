#Dictionaries in python are a datatype to store a collection of key-value pairs

#features:
#--- Mutable : you can manipulate the data without moving it to a new location in memory
#--- Key-Value-Pairs : instead of indices painting to items in a collection, we have 
# labels (keys) that point to items (values)
#--- They are unordered "Technically"

#features of key-value pairs (kvp)
#-- keys must be unique (one key -> one value)
#-- Keys are typically strings (can be other immutable datatypes like string, integer, etc)
#--- Values are FLexible, and can change (And can be just about any datatype)
#-- You can have duplicate values


#--- Creating Dictionaries using curly braces

empty_dict = {} #use curly braces when define dictionary

#defining a populated dictionary

#syntax
#dictionary = {key: value, key2: value2}

kitchen = {
    'drawer': "silver ware", #keys and value separated by colon:, whole kvps seperated by comma
    "pantry":"snacks", 
    "cabinet": "plates"
    }

print(kitchen)

#---- Accessomg Values from Dictionaries
#syntax
#dictionary[key] returns the value of the key

print(kitchen["drawer"])

#KeyErrors - trying to use a key that doesnt exist

#print(kitchen['fridge']) # IT GIVES KEYERROR

# A way to avoid KeyErrors is to use .get()

print(kitchen.get("pantry")) #Returns snacks
print(kitchen.get("fridge")) #Returns None since fridge is not a key in my dict

#add custom message to be displayed in the event you use a bad key

print(kitchen.get("fridge", "BAD KEY!!!"))

#can store keys in variables to be used

my_key = 'cabinet'

print(kitchen.get(my_key))
print(kitchen.get(my_key, "f'{my key} is not a key in your dictionary'"))

