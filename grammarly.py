from textblob import TextBlob

a = TextBlob("campk12 is a good compny")
b = TextBlob("eleehants are samll")
a = a.correct()
b = b.correct()
print(a)
print(b)