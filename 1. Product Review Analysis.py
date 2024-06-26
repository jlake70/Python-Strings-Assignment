# Task 1
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
    review = review.replace("poor", "POOR")
    review = review.replace("average", "AVERAGE")

    return review
for review in reviews:
        print(keyword_highlighter(review))

