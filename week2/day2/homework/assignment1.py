# 1. Product Review Analysis
# Objective:
# The aim of this assignment is to extract insights from product reviews by using string manipulation to categorize 
# and summarize customer feedback for a SaaS product.

# Task 1: Keyword Highlighter

# Write a program that searches through a series of product reviews for keywords such as 
# "good", "excellent", "bad", "poor", and "average". Print out each review with the keywords in uppercase so they stand out.

print('''
      Task 1
      ''')


python_reviews = [ "This product is really good. I'm impressed with its quality.", "The performance of this product is excellent. Highly recommended!", "I had a bad experience with this product. It didn't meet my expectations.", "Poor quality product. Wouldn't recommend it to anyone.", "The product was average. Nothing extraordinary about it." ]

keywords = ['good', 'excellent', 'bad', 'poor', 'average']

uppercase_review = []
sentence = ""

for reviews in python_reviews:
    split_reviews = reviews.split()
    for word in split_reviews:
        # print(word)
        z = 0
        if word[-1] == ".":
            z = 1
            word = word.rstrip(".")
        elif word[-1] == ",":
            z = 2
            word = word.rstrip(",")
        i = 0
        for keyword in keywords:
            if keyword.lower() == word.lower():
                i = 1
        if i == 0:
            sentence += ' '+word
        elif i == 1:
            sentence += " "+word.upper()
        if z == 1:
            sentence += "."
        elif z == 2:
            sentence += ","
    # print(sentence)
    uppercase_review.append(sentence.lstrip())
    sentence = ""
    
print(uppercase_review)

# Task 2: Sentiment Tally

# Develop a function that tallies the number of positive and negative words in each review. 
# Use a predefined list of positive and negative words to check against. 
# The function should return the count of positive and negative words for each review.

print('''
      Task 2
      ''')

python_positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"] 
negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]

positive_count = 0
negative_count = 0

def positiveb(worda):
    i = 0
    for positive_word in python_positive_words:
        if worda.lower() == positive_word.lower():
            i += 1
        else:
            pass
    return i
        
def negativeb(wordb):
    i = 0
    for negative_word in negative_words:
        if wordb.lower() == negative_word.lower():
            i += 1
        else:
            pass
    return i

python_reviews = [ "This product is really good. I'm impressed with its quality.", "The performance of this product is excellent. Highly recommended!", "I had a bad experience with this product. It didn't meet my expectations.", "Poor quality product. Wouldn't recommend it to anyone.", "The product was average. Nothing extraordinary about it." ]

keywords = ['good', 'excellent', 'bad', 'poor', 'average']

uppercase_review = []
sentence = ""

for reviews in python_reviews:
    split_reviews = reviews.split()
    for word in split_reviews:
        # print(word)
        z = 0
        if word[-1] == ".":
            z = 1
            word = word.rstrip(".")
        elif word[-1] == ",":
            z = 2
            word = word.rstrip(",")
        i = 0
        for keyword in keywords:
            if keyword.lower() == word.lower():
                i = 1

        # print(positiveb(word))
        # positive_return = positiveb(word)
        positive_count = positive_count + int(positiveb(word))
        negative_count = negative_count + int(negativeb(word))
        if i == 0:
            sentence += ' '+word
        elif i == 1:
            sentence += " "+word.upper()
        if z == 1:
            sentence += "."
        elif z == 2:
            sentence += ","
    # print(sentence)
    uppercase_review.append(sentence.lstrip())
    sentence = ""
    
print(uppercase_review)
print("Total number of Positive Reviews:",positive_count)
print("Total number of Negative Reviews:",negative_count)


# Task 3: Review Summary

# Implement a script that takes the first 30 characters of a review and appends "…" to create a summary. 
# Ensure that the summary does not cut off in the middle of a word.

print('''
      Task 3
      ''')

summary_reviews = []

for reviews in python_reviews:
    summary_1 = reviews[:30]
    i = 30
    while summary_1[-1] != " ":
        i += 1
        summary_1 = reviews[:i]
    summary_1 = summary_1 + "..."
    summary_reviews.append(summary_1)

print(summary_reviews)