#Nesting Dictionaries and Lists

#Lists inside Dictionaries

pet_names = {
    'Dogs' : ["Oreo", 'Bailey', 'Fido', "Pumpkin", 'Baby', 'Trouble'],
    'Cats' : ['Mittens', 'CatKeisha', 'Snowball', 'Cookie', 'Smokey'],
    'Hamster' : ['Cheddars', 'Hamtaro', 'Lightning', 'Turbo', "Hammie"],
    'Lizards' : 'Lizzy'
}

#we can chain keys and indices one after another
print(pet_names['Cats'][3])

for pet, names in pet_names.items():
    print(f"\nCommon {pet} names:")
    if isinstance(names, list):
        for name in names:
            print(name)
    else:
        print(names)


#Dictionaries inside of Lists:

books = [
    {"Title": "Dairy of a Wimpy Kid", "Author" : "Jeff Kiney", "Genre" : "IDK"},
    {"Title" : "Rich Dad Poor Dad", "Author" : "Robert Kiwaske", "Genre" : "Self Help"},
    {"Title" : "Dune", "Author" : "Frank Herbert", "Genre" : "Science Fiction"}
]

print(books[0]["Author"])

for book in books:
    print(f"{book["Title"]} is written by {book["Author"]}")

#Dictionaries within dictionaries

user = {
    "dk@email.com" : {'username':"dylank", 'password':'12345', 'likes':["tacos", "dogs"]},
    "tp@gmail.com" : {"username":"travisp", "password":"67890", "likes":["key lime pie", "Walks on the beach"]},
    "rk@dogmail.com" : {"username" : "Rhiannon-Bananan", "password" : "password", "likes":["treats", "Walks on the beach"]}
}

print(user["tp@gmail.com"]["likes"][0])


def login(user_dict):
    while True:
        try:
            email = input("Email: ")
            password = input("Password: ")

            user = user_dict[email]
            pw = user_dict[email]["password"]
            # print(user)
            # print(pw)
            if password != pw:
                # print("Bad Password")
                raise ValueError
        except:
            print("Invalid Email or Password")
        else:
            print(f"Welcome back {user['username']}")
            break


login(user)

