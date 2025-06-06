from textblob import TextBlob
from newspaper import Article
# extraction du Text depuis un URL
url = 'https://en.wikipedia.org/wiki/Economy'
article = Article(url)
article.download()
article.parse()
article.nlp()

texte = article.text
summary = article.summary

print("\n===========================\n")
print("texte complet depuis l'URL :\n", texte)
print("\n===========================\n")
print("résumé depuis l'URL :\n", summary)

# Analyse du sentiment pour le texte extrait de l'URL
blob = TextBlob(texte)
sentiment = blob.sentiment.polarity

print("sentiment depuis l'URL : ", sentiment)

# extraction du text depuis le fichier 'sentiment.txt'
with open('lib/sentiment.txt', 'r') as fic:
    texte2 = fic.read()

blob2 = TextBlob(texte2)
sentiment2 = blob2.sentiment.polarity

print("\n===========================\n")
print("texte depuis le fichier existant :\n", texte2)
print("\n===========================\n")
# analyse du sentiment pour le texte extrait du fichier .txt
print("sentiment depuis le fichier existant : ", sentiment2)


