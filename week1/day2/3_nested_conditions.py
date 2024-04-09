#Nested if's, or if statements inside if statements

#ACtivity of the day

weather = "sunny"
friends_and_i = 2

if weather == "sunny":

    if friends_and_i >=6:
        print("LEts play volleyball")
    elif friends_and_i == 5:
        print("Frisbee")
    else:
        print("The", friends_and_i, "of us should play GOLF")
else:
    print("Lets go to movies")