#String Formatting allows us to embed variables directly into string

#f string

flavor = 'Moose Tracks'
food = 'Ice Cream'

statement = f'My Favourite {food} flavour is {flavor}'
print(statement)

# .format()

city = 'Atlanta'
team = 'Falcons'

info = 'The {} are from {}.'.format(team, city)
print(info)

#Advanced f strings, embedding full inline expressions

name = "Harsh"
#We can conditionally add space before the name using concatentation
greeting = f"Hello there{' '+name if name else ''}, how are you doing?"

print(greeting)

