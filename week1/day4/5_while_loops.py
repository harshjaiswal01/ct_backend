#While loops allow us to repeat code while a condition is true

#it will continue to run until that condition is False or we break out of loop

#syntax

#while (condition):
#   code block

bus = []

#my bus can only fit five people

while len(bus) < 5:
    print('Letting a person on')
    bus.append(input("Passenger Name: "))

print(bus)

#Need to be careful about infinit loops

#Another thing, failute to launch
#meaning the loops condition starts as false and never run

while len(bus) > 5:
    print('Letting a person on')
    bus.append(input("Passenger Name: "))

