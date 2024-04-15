#intro to For Loops

#Allow us to execute a code block for every item in an iterable

#They allow us to repeat a code a limited number of times (number of times is determined by the iterable)

#Sytax of For Loop 

#for item in iterable:
#   Code block

flavors = ['Vanilla', 'Chocolate', 'Mint', 'Caramel']

for flavor in flavors:
    print('Running Code Block')
    print(flavor)

guest_list = ['Dylan', 'Travis', 'Christian', 'Sarah', 'Shoha']

line = ['Adam', 'Craig', 'Dylan', 'Travis', 'Billy Bob']

#doorman for loop

for person in line:
    print("*", person, 'walks up *')
    if person in guest_list:
        print("Welcome to the party", person)
    else:
        print("Scrammm", person)


nums = [12, 3434, 1239, 24324, 3423, 23234, 323, 2343]

for num in nums:
    if num % 2 == 0:
        print(num, 'is an even number')
    else:
        print(num, "Is an odd number")

