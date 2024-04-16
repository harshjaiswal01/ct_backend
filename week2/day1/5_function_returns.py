#The goal of many functions is to produce something
#-- take something in as an argument
#-- manipulate it or do something with it
#-- and return the output

#simple function

def addition(a, b):
    # print(a + b)
    return a + b

total = addition(2, 2)
print(total)

# doubler function takes in a list of nums and doubles all the nums and returns a list if double nums

def doubler(nums):
    output = []
    for num in nums:
        doubled_num = num*2
        output.append(doubled_num)
    return output #return causes your function to terminate and returns whatever value is there

my_nums = [1, 2,3, 4,5,6]
dnums = doubler(my_nums)
print(dnums)

#---- No Return

def greet_card(name):
    print(f"HAve a nice day {name}")

card_message = greet_card("Travis")
print(card_message) # IT prints none because no return

