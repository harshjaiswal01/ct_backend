#Inclass 1

# PROBLEM STATEMENT
#An online bookstore is processing orders for a popular novel. They need a simple system to ensure that customers enter a valid quantity when placing their orders.

# Instructions

# 1. Prompt the user to enter the quantity of books they wish to order
# 2. Validate the input to ensure it is a positive integer
# 3. If the input is valid, confirm the order by printing a message
# 4. If the input is invalid (not an integer or a negative number), display an error message and prompt the user again
# 5. Use a try/except block to catch non-numeric inputs

# using input() ask user how many books

#check type() of input or isinstance(), rely on try except to handle invalid input

#else block to show a order confirmation message, if try block succeeds

#except : to handle invalid data and respong with error message
#--- ValueError : If they give a 'nine' instead or 9
#--- reaise ValueError : specific value error for negative

#While look to contrinuously ask and only break once they succeed

while True:
    try:
        num_books = int(input("How many books do you wish to order: "))
        if num_books < 0:
            raise ValueError('no negative values')
    except ValueError as ve:
        if 'no negative values' in str(ve):
            print("No negative values")
        else:
            print("Please enter a positive numeric value like 1")
    else:
        print(f"Your order is confirmed for {num_books} books")
        break
