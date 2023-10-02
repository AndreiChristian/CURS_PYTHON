from textblob import TextBlob

reviews = [
    "I love this product. It's amazing!",
    "The experience was terrible. I'm very disappointed.",
    "Overall, it was an okay experience. Not the best but not the worst either.",
    "I have nothing but good things to say about this!",
    "This is just a waste of money."
]

for review in reviews:
    blob = TextBlob(review)
    polarity = blob.sentiment.polarity
    subjectivity = blob.sentiment.subjectivity

    if polarity > 0:
        sentiment = 'Positive'
    elif polarity < 0:
        sentiment = 'Negative'
    else:
        sentiment = 'Neutral'

    print(
        f"Review: {review}\nSentiment: {sentiment}, Polarity: {polarity}, Subjectivity: {subjectivity}\n")
