#--- Adding and updating KVPS

kitchen = {
    'drawer': "silver ware",
    "pantry":"snacks", 
    "cabinet": "plates"
    }

#-- add a kvp

#dictionary[new_key] = new_value

kitchen['fridge'] = 'cold stuff'

print(kitchen)

kitchen["freezer"] = "Frozen stuff"

print(kitchen)

#-- updating the value of a key

#dictionary[existing_key] = new_value

kitchen["cabinet"] = "plates and bowls"
print(kitchen)

#-- incrementing values

stock = {'oranges' : 10, 'apples': 2, 'pears': 20}

#need to restock in apples 10 more

stock['apples'] += 10
print(stock)

#--- .update({key, value}) : merges one dictionary into another, updating any common keys to the new values
#updating any common keys to the new values

car = {"year": 1968, "Make" : "Ford", "Model" : "Mustang"}
car.update({"color":"green"}) #adding kvps with .update()

print(car)
car.update({"color":"black"}) #updating kvps with update()
print(car)

car.update({"wheels":4, "engine":"v8", "year":2024})
print(car)


