#---Inline if statements aka Ternary Operators, A way to write if statements in a single line

#Syntax
#if_output if (condition) else else_output

candy_jar = 'full'

print("Its Candy Time" if candy_jar == 'full' else 'Time to get it')


#inline with and

candy_jar = 'full'
sweet_tooth = True

print("Its Candy Time" if candy_jar == 'full' and sweet_tooth else 'Time to get it')

#inline with and

candy_jar = 'fulli'
sweet_tooth = False

print("Its Candy Time" if candy_jar == 'full' or sweet_tooth else 'Time to get it')