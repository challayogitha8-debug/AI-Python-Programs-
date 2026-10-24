
import nltk
from nltk.stem import PorterStemmer

# Initialize the stemmer
stemmer = PorterStemmer()

# Example sentence to be stemmed
sentence = "The quick brown foxes jumped over the lazy dog."

# Tokenize the sentence
tokens = nltk.word_tokenize(sentence)

# Apply stemming to each token in the sentence
stemmed_tokens = [stemmer.stem(token) for token in tokens]

# Print the original sentence and the stemmed sentence
print("Original sentence:", sentence)
print("Stemmed sentence:", " ".join(stemmed_tokens))

