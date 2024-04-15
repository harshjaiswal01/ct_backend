#Special moves

#Break, Continue, and Pass

#-- Break : terminates a list prematurely

pay_dirt = ['dirt', 'dirt', 'dirt', 'gold', 'dirt', 'dirt']

for scoop in pay_dirt:
    print("Panning for Gold")
    if scoop == 'gold':
        print("We found GOLD")
        break
    else:
        print("Just more dirt, gotta keep looking")


#-- Continue : Continue skips the rest of the code block and moves on to the next iteration

#square odd numbers
nums = [13, 256, 1146, 478, 21, 3457]

for num in nums:
    if num % 2 == 0:
        continue
    num **= 2
    print(num)

#PAss

my_list = [1, 2, 3]

for item in my_list:
    pass
