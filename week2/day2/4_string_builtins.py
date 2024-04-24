#String built ins. reminder strings are immutable, so none of these are modifying the original strings

#-- len() : Returns the number of characters in a string including whitespace and symbols

phrase = "I am in love"

print(len(phrase))

#-- upper() : Uppercases all the letters in the string

phrase = "Wow it is really nice"
yell_phrase = phrase.upper()
print(yell_phrase)

#-- lower() : return the full lowercase version of entire string

phrase = 'Wor look at all these BOOKS!'
inside_voice = phrase.lower()

#-- title() : formats strings in a Title Case, capitalizing every word seperated by a space

person = 'abraham lincoln'
print(person.title())

#-- replace(substring, replacer, how_many_times = all) : replace a substring of a string with a replacer

am = 'Good Morning'
pm = am.replace("Morning", "Evening")

print(pm)

am = 'Good Morning Moring'
pm = am.replace("Morning", "Evening", 1)

print(pm)

#-- strip() : removes unwanted text from either side of a string, default to remove whitespace. No need to add anything for whitespace

class_146 = "                            WOO THIS CLASS ROCKS                   "
print(class_146)
print(class_146.strip())

#can tune to strip specific characters

gibberish = ' *gg*Gsdfs#2342fs#$#%@#$ Diamond in the rough @#$@$@#$@# '
print(gibberish.strip(" @#$@#$@#$@#$56%$*gGsdf2342"))

#-- lstrip() : Only works on the left side. works just like strip()

#-- rstrip() : Only right side



#-- .find(sub_string) : returns the start index of the substring

jungle = "There is a Tiger in my jungle"

print(jungle.lower().find("tiger"))

#-- .count(sub) : counts the occurances of the substring in the main string

green = "Green in my favourite color. I like gree trees, green lime, green crap"

print(green.lower().count("green"))

#-- startswith(sub) : returns True or False depending on whether the string starts with sub or not

name = "Jeffery"
print(name.lower().startswith("j"))

people = ['Alex', 'Aj', 'Brian', 'Clinton', 'Gerardo', 'Harsh']

a_team = []
for student in people:
    if student.lower().startswith("a"):
        a_team.append(student)

print(a_team)

#--endswith(sub) : returns True or False depending on whether the string ends with sub or not

name = "Travis"
print(name.endswith("s"))

#un-inviting the Freys from the wedding

guest_list = ["Rob Stark", "Caitlyn Stark", "Jorah Mormont", "Walder Frey", "George Frey", "Arthur Tully"]

#un-invite

new_list = []
for guest in guest_list:
    if not guest. lower().endswith("frey"):
        new_list.append(guest)

print(new_list)

#Three string checkers

#-- isalpha() : returns true if the string is made entirely of alphabetic character

letter = 'A'
print(letter.isalpha())

#-- isdigit() : Returns True if string is made entrily of numeric characters

nums = '12345'
print(nums.isdigit())


#-- isspace() : returns true if string if comprised of only whitespace

word = 'My Test Variable'
snake_case = ""
for letter in word:
    if letter.isspace():
        snake_case += '_'
    else:
        snake_case += letter
print(snake_case)

#-- .split(sub) splits your string based on a specified substring into a list of strings, default split on space

words = "This is one big string with many words"

words_list = words.split()
print(words_list)

flavors = input("Tell me all favourite flavors seperated with space").split()
print(flavors)

#--- MEmbership checks in strings, checking if a substring is in a string
# in

magic_word = 'blueberry'
sentence = "Im having blueberry pancakes for dinner!"

if magic_word in sentence:
    print("We got Blueberry")

    