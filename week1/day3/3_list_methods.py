#Some of the cool things we can do with list methods

food = ["Tacos", "Pizza", "Butter Chicken", "Potato"]
print(food)

#-- list.append() : adds items to the end of list
print("Adding Ice Cream")
food.append("Ice Cream")
print(food)

#-- .insert(idx, item) : Needs to know which location and what item

food.insert(0, "Cake")
print(food)

#-- .remove(item) : Removes the first occurance of an item

print("Eating all the Pizza and removing")

#-- will give valueError if item doesnt exist in list (case sensitive)

food.remove("Pizza")
print(food)

#-- .pop() : removes and returns the last item in the list
#just because it returns a value doesnt mean I to collect the value in a variable

print("Popping ice cream into the freezer")

freezer = food.pop()
print("Freezer: ", freezer)
print(food)

#-- .pop(idx) : removes using index(location)

print("Popping potato into oven")

oven = food.pop(-1)
print(food)
print("Food in Oven:", oven)



food.append("Key lime pie")
food.append("Cheese")
food.append("Burger")
food.append("Salad")
food.append("Sushi")
food.append("Burger")

print("Hit the store!")
print(food)

#-- .index(item) : Will find the position and return it as int

print("Finding the position of Salad using .index().")
salad_idx = food.index("Salad")
print("Salad Position", salad_idx)

#-- Modify the values at a particular position/index Mutability list[index] = new_item

print("Spicing up our Salad")
food[6] = "Ceaser Salad"

print(food)

#-- list.count(item) : Will count the occurances of an item in a list, returns an int

print("Counting Burgers!")
burger_count = food.count("Burger")
print("Burger Count:", burger_count)

#-- list.reverse() : Will reverse the order of the list
food.reverse()

print(food)

#-- list.sort() will sort your list in ascending if numbers or alphabetical order for string

print("Sorting in Alphabetical Order")
food.sort()
print(food)

#-- list.sort(reverse = True) reverse sort

food.sort(reverse=True)
print(food)

#------- LIST FUNCTIONS

#-- len() : Returns the length of the list

print("Length of Food list:", len(food))

#-- sum() : give the sum total of all the numbers in a list
#list must be entirely made of ints and/or floats

nums = [1, 2, 4, 1, 9.3]
total = sum(nums)
print(total)

