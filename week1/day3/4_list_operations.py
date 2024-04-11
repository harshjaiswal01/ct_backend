#Other cool things to do with lists

#Membership checks using 'in' to check if an item is in a list, returns a boolean value

guest_list = ["Adam", "Bob", 'Charlie', 'Dylan', 'Ethan']

print('Albert' in guest_list)
print('Dylan' in guest_list)

name = input("Name of the guest? ")

#if statements with menbership checks

if name in guest_list:
    print("Welcome to the party!!!")
else:
    print("Sorry, next time")


#Merging two list with '+'

list_1 = [1, 2, 3, 4]
list_2 = [5, 6, 7, 8]
list_3 = list_1 + list_2
print(list_3)

#copying a list using .copy()

fruit = ["Apple", 'Orange', 'Banana']
copy_fruit = fruit.copy() # or fruit[:]
print(copy_fruit)
copy_fruit.pop()
print(copy_fruit)

#Common mistakes when trying to make copies, setting one list - to another

nums = [1, 2, 3, 4]
dnums = nums # This means whatever you do to dnums happens to nums. so dont use it like this. its one data with two names
print(dnums)
dnums.pop()
print(dnums)
print(nums)

#Identity operators 'is' and 'is not', returns a boolean value

print(nums is dnums)
print(fruit is copy_fruit)

#List slicing --- list[start:stop] returns a sublist from start to stop index
#default for start and stop are the beginning and end of the list
#the stop index is non-inclusive, meaning the item located in the stop index wont be included in the slice

key_lime_pie = ['slice1', 'slice2', 'slice3', 'slice4']

my_slice = key_lime_pie[0:1]
print(my_slice)

big_slice = key_lime_pie[1:3]
print(big_slice)

last_slice = key_lime_pie[3:4] #or key_lime_pie[3:] or key_lime_pie[-1:]
print(last_slice)


#Joining a list of strings ''.join(list)

words = ["Hello", 'Im', 'getting', 'joined!']

sentence = ' '.join(words) #' '.join(list) put a space to get spaced out or however you want to join

print(sentence)
