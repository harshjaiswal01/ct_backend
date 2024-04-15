#nested loops

#A Loop inside of a loop

#because the inner loop is in the code block of outer loop
#the inner loop will run to completion every time the outer loop interates once

nums = [1,2, 3,4]

for num1 in nums:
    print('Outer loop iteration:', num1)
    for num2 in nums:
        print("Inner loop iteration:", num2)

#-- Topping Combination

topping = ['Pepperoni', 'Sausage', 'Ham', 'Pineapple', 'Olives']

for topping_1 in topping:
    for topping_2 in topping:
        if topping_1 == topping_2:
            print("Double", topping_1)
        else:
            print(topping_1, topping_2)

