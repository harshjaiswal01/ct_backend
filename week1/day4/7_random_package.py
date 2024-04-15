import random #import random as r or from random import randint, shuffle and use randint and shuffle directly

#Random package, imports alot of functions that give us the thrill of chance

#random.randint(start, stop) will give you a random number betweem the start and stop INCLUSIVE

#DICE
print(random.randint(1, 6))

players = ['Dylan', 'Clinton', 'Harsh']

for player in players:
    roll = random.randint(1,6)
    print(player, "Rolls a", roll)

# .shuffle(list) mixes the order of the list randomly

chores = ['Dishes', 'Laundry', 'Dust', 'Take dog out']

random.shuffle(chores)

print('This is the order I am doing my chores')
for chore in chores:
    print(chore)

#-- .choice(List) returns a random item from that list

game = ['Rock', 'Paper', 'Scissors']

while True:
    my_choice = input('Rock, Paper, Scissors, Shoot ')
    computer = random.choice(game)
    print('Computer chose:', computer)
    win = input('Did you win? yes or no? ')
    if win == 'yes':
        print('Nice Work')
        print('According to you', my_choice, 'beats', computer)
        break

