#add 2 nums

def add(x,y):
    z = x+y
    return z

#subtract 2 nums

def sub(x,y):
    return x-y

#multiply 2 nums

def mul(x,y):
    return x * y

#divide (catching 0 division error) 2 nums

def div(x,y):
    if y != 0:
        return x/y
    else:
        return 0
    
    