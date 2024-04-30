import re #make sure to import re i.e. regex

#-- re.findall(oattern, text) : retreives all non-overlapping data and matches the pattern
#and returns a list

text = 'Hi my name is Dylan, and I like to go and do things and stuff'

ands = re.findall(r'and', text)
print(len(ands))

#find all hashtags in post

post = 'I LOVE # learning #Python and #Regex, this is so fun! #Coder'
hash_tags = re.findall(r'#\w+', post)
print(hash_tags)


#find all words that start with letter b and end with letter e

sentence = 'Abe asked to build a bridge but he was told "beware of the beehives!".'

bes = re.findall(r'\bb\w*e\b', sentence)

print(bes)

#finding emails

text = 'You can contact me at d-k@gmail.com or d.ylank@codingtemple.com'

emails = re.findall(r'[\w._-]+@[\w._-]+\.[a-z]{2,3}', text)

#USername and domain can include letters a-z, digits, _, -, .

print(emails)

#-- re.search(pattern, text) : Searched a string for a pattern match and return
#the first occurance as a match object

# email = input("Enter email: ")
email = 'hj@gmail.com'
found = re.search(r'[\w._-]+@[\w._-]+\.[a-z]{2,3}', email)

# print(found.span())
# print(found.group())

if found:
    print(f'{found.group()} is a valid email')
else:
    print('Invalid Email')

#Validating phone numbers

# 000-000-0000
# 000 000 0000
# 0000000000
# (999) 999 9999

number = '(720)-618  9405'

phone = re.search(r'[(]?\d{3}[)]?[-|\s]?\d{3}[-|\s]?\d{4}', number)

print(phone)

#-- re.match(pattern, text) : Will return a match object if there is a 
#pattern match at the very beginning of the text

text = 'Hello, World'

obj = re.match(r'Hello', text)
print(obj)


#check to see if a website is secure
#https or http

url = 'https://www.codingtemple.com'

secure = re.match(r'https',url)
print('Secure' if secure else 'Not Secure')

#-- re.split(pattern, text) : splits the text on occurances of the pattern,
#returns a list

#split on the garbage
text = 'Python,Regex;Splitting-Example. Fun, right?'
words = re.split(r'[,.;?-]+', text)
print(words)

#-- re.sub(pattern, replacer, text) : replaces occurances of the pattern in 
#a string with a replacer
number = '(720)-618 9405'

formatted_number = re.sub(r'\D', '', number)
print(formatted_number)

#Anonymous chat

chat = '''
@Dylank123 : "I think I love regex"
@Travis : "Dont you have a wife"
@Dylank123 : "Its just not the same"
@Travis : "She better not see this!"
'''

anon_chat = re.sub(r'@\w+', '@User-anon', chat)
print(anon_chat)

