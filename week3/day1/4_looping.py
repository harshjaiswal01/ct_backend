#looping over tuples is the exact same as looping over lists

#write a function that loops over a gived tuple

def tup_loop(atuple):
    for item in atuple:
        print(item)


my_tup = 'Apple', 'Banana', 'Orange'

tup_loop(my_tup)

def while_tup(atuple):
    i = 0
    while i < len(atuple):
        print("\n",atuple[i])
        i += 1

while_tup(my_tup)

#-- enumerate() that allows you to iterate over the index and item at the same time

today = 'woke up', 'ate breakfast', 'walked my dog', 'prepped lecture', 'ate lunch', 'graded', 'meetings', 'in class'

for task in enumerate(today): #task is a tuple of the index and item
    print(task)
    print(f'{task[0] + 1}: {task[1]}') #Its printing index and stuff in it and adding 1 so that it doesnt start from 0


for idx, task in enumerate(today):
    print(f'{idx + 1}:{task}')

