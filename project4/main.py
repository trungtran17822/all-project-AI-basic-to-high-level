from textblob import TextBlob
# from newspaper import Article

# url = 'https://www.cnbc.com/2025/08/06/10-year-treasury-yield-ticks-higher-ahead-of-bond-auctions.html?&qsearchterm=dow%20rises'
# article = Article(url)

# article.download()
# article.parse()
# article.nlp()

# text = article.summary
# print(text)
with open('mytext.txt', 'r') as f:
    text = f.read()
blob = TextBlob(text)
sentiment = blob.sentiment.polarity  # -1 to 1
print(sentiment)
