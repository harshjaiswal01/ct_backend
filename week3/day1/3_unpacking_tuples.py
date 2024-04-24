#Unpacking Tuples

#packing tuples reminder

packed = 'bacon', 'lettuce', 'tomato'
print(packed)

#basic unpacking
first, second, third = packed #Variables need to exact. Will throw a ValueError if vars and items are not equal
print(first)

#Variables need to exact. Will throw a ValueError if vars and items are not equal
#-- too many values to unpack
#-- not enough values to unpack

#extended Unpacking : takes additional var less values and packs them into a list

enhanced_blt = 'bacon', 'lettuce', 'tomato', 'mayo', 'avocado', 'everything bagel seasoning'
print(enhanced_blt
      )
first, second, third, *condiment = enhanced_blt
print(first)
print(second)
print(third)
print(condiment)
first, second, third = condiment
print(first)
print(second)
print(third)

#You cant have multiple * expressions or you'll get a SyntaxError

