#-- Extracting List Data
import re

flowers = []

with open('garden.txt', 'r') as file:
    for line in file:
        flowers.append(line.strip())

print(flowers)
golf_clubs = {}
with open('golf_bag.txt', 'r') as file:
    for line in file:
        club, brand = line.strip().split(': ')
        print(club)
        print(brand)
        golf_clubs[club] = brand
print(golf_clubs)

#Extracting Denser Data = Books

def read_books():
    books = {}
    with open('books.txt', 'r') as file:
        for line in file:
            title, author, genre, desc = line.strip().split('-:-')
            books[title] = {'Author':author, 'Genre':genre, 'Desc':desc}
    return books

my_books = read_books()
print(my_books)

def add_books(books):
    with open('books.txt', 'w') as file:
        for title, info in books.items():
            file.write(f'{title}-:-{info['Author']}-:-{info['Genre']}-:-{info['Desc']}\n')

def edit_book():
    books = read_books()
    title = input('What Book do you want to change?')
    if title in books:
        desc = input('Give a new Description: ')
        books[title]['Desc'] = desc
        add_books(books)

edit_book()
