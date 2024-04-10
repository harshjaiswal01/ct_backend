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
copy_fruit = fruit.copy()
print(copy_fruit)
copy_fruit.pop()
print(copy_fruit)