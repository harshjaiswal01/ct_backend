#In python you have two kinds of scope, Global scope and local scope

#The scope determines what variables are accessible

#Global Scope is anywhere outside of your functions

x = 7 #all these variables are considered to be global variables and can be accessed anywhere in your code
a = "Words"
alist = ['item', 'item', 'item']

if x:
    print(x)

#Local scope is created inside of functions

def local_func():
    y = 7 #This is a local variable and can only be referenced within this function
    print(x) #Can call global variables into local scope

print(y) #Cannot call local variables into global scope, It will give error


