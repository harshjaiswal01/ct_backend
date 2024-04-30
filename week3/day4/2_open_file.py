#Write to a file

file = open('new_file.txt', 'w')
file.write('Writing to a file from Python!!!')

file.close()

#Overwriting Files

file = open('new_file.txt', 'w')
file.write("Overwriting\n")
file.close()

#Adding to a file(Without Overwriting)

file = open('new_file.txt', 'a')
file.write("\nAdding stuff")
file.close()

#reading files

file = open('new_file.txt', 'r')
content = file.read() #returns a large string of the entire text
# lines = file.readlines() #returns a list of items defined by new lines 
# print(lines)
print(content)
file.close()


#-- with : allows us to open files to a codeblock and automatically close files
#when the codeblock is exited

with open('new_file.txt', 'r') as file:
    content = file.read()
    print(content)

with open('new_file.txt', 'r') as file:
    for line in file:
        print(line.strip()) #Strip this way removes the \n from the end of the line

#-- Store Data from a list

flowers = ['Wysteria', 'Sun Flowers', 'Rose', 'Orchids']

with open('garden.txt', 'w') as file:
    for flower in flowers:
        file.write(flower+'\n')

#-- Storing Dictionary Data

clubs = {'Driver':'Cobra', 'Irons':'Sirixon', 'Hybrid':'Callaway', 'Putter':'Ping'}

with open('golf_bag.txt', 'w') as file:
    for club, brand in clubs.items():
        file.write(f'{club}: {brand}\n')

#-- Storing Book
#{title:{author: name, genre: name, description : summary}}

books = {
    'Green Lights': {'Author':'Mathew McConaughey', 'Genre':'Biography', 'Desc' : 'fun book, I really love this book.'},
    'More than a Carpenter': {'Author':'Josh Mcdowell', 'Genre':'Christian Literature', 'Desc' : 'fun book, I really love this book.'},
    'Diary of a Wimpy Kid': {'Author':'Jeff Kinay', 'Genre':'YAF', 'Desc' : 'fun book, I really love this book.'},
    'Black Flags': {'Author':'Joby Ray', 'Genre':'NonFiction', 'Desc' : 'Potentially, this is a story about pirates'}
}

def add_books(books):
    with open('books.txt', 'w') as file:
        for title, info in books.items():
            file.write(f'{title}-:-{info['Author']}-:-{info['Genre']}-:-{info['Desc']}\n')

add_books(books)
