# 2. Python Data Structure Challenges in Real-World Scenarios
# Objective:
# This assignment is designed to enhance your understanding and application of 
# Python's core data structures - tuples, lists, and dictionaries - in real-world contexts. 
# By engaging with these tasks, you will practice manipulating these data structures, 
# applying built-in Python methods, and implementing error handling in practical situations.

# Task 1: Library System Enhancement
# Sharpen your skills in managing and modifying data within tuples and lists.

# Problem Statement:
# You are maintaining a library system where each book is stored as a tuple within a list. 
# Your task is to update this system by adding new books and ensuring no duplicates.

# Existing Library Data:

library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]
# Add functionality to insert new books into library.
# Ensure that adding a duplicate book is handled appropriately.

def add_to_library(book_name, author, library_complete):
    ch = 0
    library_new = []
    for books in library_complete:
        if book_name == books[0] and author == books[1]:
            ch = 1
    if ch == 1:
        print("Sorry. This book is already in library")
        library_new = library_complete
    else:
        library_new = library_complete + [(book_name, author)]
        print("Book has been added to the library")
    return library_new

def remove_from_library(book_name, author, library_complete):
    ch = 1
    for books in library_complete:
        if book_name == books[0] and author == books[1]:
            # print("Book found in Library")
            ch = 0
    if ch == 1:
        print("Sorry. This book is not in the library")
    else:
        book_tup = (book_name, author)
        index = library_complete.index(book_tup)
        # print("Index is ", index)
        library_complete.remove(book_tup)
    return library_complete

while True:
    try:
        print('''
              Welcome to your Library! Please select from one of the following choices:
              1. Add a book to Library
              2. Check out a book from Library
              3. See the books in Library
              4. Exit Library
              ''')
        choice = int(input("Please input your choice - 1 or 2 or 3 or 4: "))
        if choice <=0:
            raise ValueError("Negative")
        if choice > 4:
            raise ValueError("Greater")
    except ValueError as ve:
        if str(ve) == "Negative":
            print("You entered a negative number. Please retry")
        elif str(ve) == "Greater":
            print("You entered a number greater than 4. Please retry.")
        else:
            print("Please retry and enter a correct value in numeric form")
    else:
        if choice == 1:
            book_name_input = input("Please enter the book name: ").title()
            author_name_input = input("Please enter the Author Name: ").title()
            library = add_to_library(book_name_input, author_name_input, library)
            # print(addbook)
            
        elif choice == 2:
            book_name_input = input("Please enter the book name: ").title()
            author_name_input = input("Please enter the Author Name: ").title()
            library = remove_from_library(book_name_input, author_name_input, library)
        elif choice == 3:
            bn = 1
            print("\nList of all books in our Library:-")
            for books in library:
                print(f"{bn}. Book Name: {books[0]}, Author : {books[1]}")
                bn += 1
        elif choice == 4:
            print("\nThank You for visiting us today. Have a great day!")
            break


