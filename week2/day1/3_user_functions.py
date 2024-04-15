#USER DEFINED FUNCTIONS

#They give us repeatable power

#Syntax

#def function_name(parameters): 
#   code block to be executed on function call

#-- Simple function

def greeting():
    print("Hello World")


greeting() #Calling a function by its name...dont forget ()


#-- function with Parameters
# establish a required variable/value for our function

def personalized_greet(name):
    print("Welcome to this world", name)

# The value that we pass in for a parameter is called an ARGUMENT

personalized_greet("Harsh")
personalized_greet("Dylan")



