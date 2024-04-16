# USER DEFINED FUNCTIONS

# They give us repeatable power

# Syntax

# def function_name(parameters): 
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

#-- More complex Example

# function to give info about ct classes

def class_info(instructors, students):
    print(f"This class is taught by {instructors[0]} and {instructors[1]}")
    class_size = len(students)
    print(f"It has {class_size} students")
    for student in students:
        print(student)

instructors_146 = ['Dylan', 'Travis']
student_146 = ['Harsh', 'AJ', 'Noach', 'Isaias', 'Mary']

class_info(instructors_146, student_146)

ins_144 = ["Ryan", 'Alex']
stus_144 = ["Billy Bob", 'BArney', "Ted", "Neha", "Lily", "Lingpi"]

class_info(ins_144, stus_144)

