#Exceptions are the other big issue that can cause your program to break/stop executing

#Exceptions : arise when our code is setup correctly but the operations dont execute for a variety of reasons

#--- NameError : try to call a var or a func before it was defined

# print(x)



#--- ValueErrors : performing operations with invalid values

# str_num = "nine"
# int_num = int(str_num) #trying to convert an invalid atribute/value

# my_list = ["apple", "banana", "orange"]
# my_list.remove("grapes") #becuase grapes are not in the list, they are an invalid value

#--- TypeError : trying to perform operations on values of innappropriate type

# num = 5
# total_people = num + ' people' #cannot add/concatenate a str and int

#--- AttributeError : trying to use methods on improper objects (the wrong datatype)

word = 'Hello'
rword = word[::-1]
print(rword)

