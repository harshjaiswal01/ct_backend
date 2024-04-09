#Recap

#We use if statements to run a particular code block, based on condition or assertion
#I want to run this code block if ...

#If checks a condition/assertion and if it is true will execute a defined codeblock

weather = 'sunny'

assertion = (weather == 'rainy')
print("Assertion is",assertion)

if weather == 'sunny':
    print("Lets have a picnic!")

porch_lit = False

if porch_lit:
    print("My path is clear")

#Compound conditional using 'and' and 'or' logical operators

#lunch windows = 12-13

time = 12.03
hungry = True

if time == 12 and hungry:
    print("Time to eat man")
else:
    print("Blah")

#taking it a step further by using range
if time >=12 and time <= 13 and not hungry:
    print("Lets go")

#changing the range to be "in between"

if 13 >= time >= 12 and hungry:
    print("Lets go again")

#--- or requires that at least one condition has to be True to execute

day = 'Saturday'

if day == "Saturday" or day == "Sunday":
    print("Not my weekend")

# using and and or together

caffinated = True
prep_lvl = 5
confidence = 100

if caffinated and prep_lvl > 6 or confidence >= 80:
    print("I am ready")

#--- Using  not logical operator

#By incorporating not our if statement runs off of False conditions

busy = True

if not busy:
    print("Time to relax")

