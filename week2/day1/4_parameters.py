# Different Types of Parameters

#Basic Parameters : assume their value from arguments passed

def name_printer(first, last, middle):
    print(f"Hello {first} {middle} {last}")

#-- Positional Arguments : The position of the argument determines which parameter it becomes the value of
name_printer("Neha", "Arora", "Lingpu")

#-- Keyword Arguments : We explicitly state which parameter takes which value
name_printer(first="Dylan", middle="Michael", last="Katina")

#-- DEfault Parameters

def tomb_stone(birth, death='TBD'):   # = Default value
    print(f'''
          This Person lived from {birth}
            to {death}
                    ''')
    
tomb_stone("6-6-1984")

tomb_stone("6-6-1984", "6-6-2184")

#One thing to note, default params need to come after all non-default params

# def breaking(broken=True, working):  THIS IS WRONG
#     pass

#--- *args : allows to take unknown number of arguments, brought into the function as a tuple

def vet_hands(staff, *vols):
    print(f"On staff today we have {staff[0]} and {staff[1]}!")
    if vols:
        print("They will be assisted by following volunteers:")
    elif not vols:
        print("No Volunteers")
    for vol in vols:
        print(vol)
vet_hands(["Dylan", "Harsh"], "Neha", "Valeshka", "Harsh", "Dylan", "Travis")

#-- **kwargs : unknown amount of keyword arguments, brought into the function as a Dictionary

def routine(**daily_events):
    print(daily_events)

routine(morning = 'I wake up and eat breakfast', mid_morning = 'I walk my dog', afternoon = 'Grading and Prepping', evening = 'I start class', night = "I chill")