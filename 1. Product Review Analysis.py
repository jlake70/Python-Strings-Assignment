# Task 1
import string

reviews = [
        "This product is really good. I'm impressed with its quality.",
        "The performance of this product is excellent. Highly recommended!",
        "I had a bad experience with this product. It didn't meet my expectations.",
        "Poor quality product. Wouldn't recommend it to anyone.",
        "The product was average. Nothing extraordinary about it."
    ]
def keyword_highlighter(review):

    review = review.replace("good", "GOOD")
    review = review.replace("excellent", "EXCELLENT")
    review = review.replace("bad", "BAD")
    review = review.replace("Poor", "POOR")
    review = review.replace("average", "AVERAGE")

    return review

for review in reviews:
        print(keyword_highlighter(review))

#Task 2
reviews = [
        "This product is really good. I'm impressed with its quality.",
        "The performance of this product is excellent. Highly recommended!",
        "I had a bad experience with this product. It didn't meet my expectations.",
        "Poor quality product. Wouldn't recommend it to anyone.",
        "The product was average. Nothing extraordinary about it."
    ]

positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
negative_words = ["bad", "terrible", "horrible", "awful", "disappointing", "subpar", "poor"]

def tally_words(reviews, positive_words, negative_words):
    positive_tally = 0
    negative_tally = 0

    for review in reviews:
        words = review.lower().split()
        for word in words:
            word = word.strip(string.punctuation)
            if word in positive_words:
                positive_tally += 1
            elif word in negative_words:
                negative_tally += 1

    return positive_tally, negative_tally

positive_tally, negative_tally = tally_words(reviews, positive_words, negative_words)

        
print("The total number of positive words: ", positive_tally )
print("The total number of negatve words: ", negative_tally )

#Task 3 
reviews = [
        "This product is really good. I'm impressed with its quality.",
        "The performance of this product is excellent. Highly recommended!",
        "I had a bad experience with this product. It didn't meet my expectations.",
        "Poor quality product. Wouldn't recommend it to anyone.",
        "The product was average. Nothing extraordinary about it."
    ]
def review_summary(review, length = 30):
    if len(review) <= length:
        return review
    
    return review[:length] + '…'
for review in reviews:                                     
    print(review_summary(review))
          
          