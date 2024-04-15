#range() creates a sequence of number that we can iterate through

#range(stop) the sequence will go from 0 to the Stop and Stop is non-inclusive

print(range(10))
print("Range to 10")
for num in range(10):
    print(num)

#--range(start, stop) : crates a sequence from start inclusive to stop non-inclusive
print("Range from 5 to 10")
for num in range(5,10):
    print(num)

for num in range(1,5):
    print(num)

#-- range(start, stop, step) : creates a range from start to stop

for num in range(10, 100, 10):
    print(num)

#-- range in combination with len

alist = ['item1', 'item2', 'item3', 'item4']

print(len(alist))

for index in range(len(alist)):
    print(alist[index])

food = ['Tacos', 'Tiramisu', 'Pizza', 'Sushi', 'Burger', 'Ceaser Salad', 'Burger', 'Key lime pie']

for index in range(len(food)):
    if food[index] == 'Burger':
        print("Burger Position is:",index)