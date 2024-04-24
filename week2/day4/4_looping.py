#Looping over dictionaries

chips = {"Cheeto" : "Flamin Hot", "Dorito" : "Cool Ranch", "Takis" : "Fuego", "Miss Vickes" : "Jalepeno"}

#looping key of a dictionary

#---- .keys() be explicit

print("Major Chip Brands")
print("-----------------")
for key in chips.keys():
    print(key)

#Looping over values of a dictionary

#----- .values()

print("\nFlavors")
print("--------------")
for value in chips.values():
    print(value)


#Looping over both key and values at the same times

print("\nMy favourite flavor per chip")
print("-------------------------------")
for key, value in chips.items():
    print(f'My favourite {key} flavor is {value}!')


