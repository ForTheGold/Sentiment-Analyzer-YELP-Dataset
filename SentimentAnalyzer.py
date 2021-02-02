import json
import random
import nltk
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords

# Open File
with open('electronics10k_formatted.json') as f:
	data = json.load(f)
f.close()

positive = []
negative = []
all_words = []

# Get words minus punctuation and stop words (also normalized to lower case below)
tokenizer = RegexpTokenizer(r'\w+')
stop_words = set(stopwords.words('english'))

# Create positive and negative lists
# Lists consist of tuples
# First part of tuple of is a list of words
# Second part is 'pos' or 'neg'
for i in range(len(data)):

	# Some list items do not contain 'overall' or 'reviewText', try/except for control
	try:
		if data[i]['overall'] > 3:
			tokens = tokenizer.tokenize(data[i]['reviewText'].lower())
			filtered = [token for token in tokens if token not in stop_words]

			# Some lists become empty because punctuation and stop words are removed
			if len(filtered) > 0:
				positive.append((filtered, 'pos'))
		else:
			tokens = tokenizer.tokenize(data[i]['reviewText'].lower())
			filtered = [token for token in tokens if token not in stop_words]
			if len(filtered) > 0:
				negative.append((filtered, 'neg'))
	except:
		continue

# There are more positive reviews than negative, reviews are shuffled to reduce bias
random.shuffle(positive)
labeled_reviews = positive[:len(negative)] + negative
random.shuffle(labeled_reviews)

# Create list of all the words, convert to frequency distribution to order by frequency, and use first 3000 most common
for review in labeled_reviews:
	for word in review[0]:
		all_words.append(word)

all_words = nltk.FreqDist(all_words)
word_features = list(all_words.keys())[:3000]

# Using a "bag of words model" where features are the presence or absence of the 3000 most common words
def find_features(document):
	features = {}
	for w in word_features:
		features[w] = (w in document[0])
	return features

featuresets = [(find_features(reviews), category) for (reviews, category) in labeled_reviews]

# 70% to train, 30% to test
training_percent = int(len(featuresets)*.7)
training_set = featuresets[:training_percent]
testing_set = featuresets[training_percent:]

# Using Naive Bayes Classifier and Printing Accuracy.  The model is typically 60~65% accurate
classifier = nltk.NaiveBayesClassifier.train(training_set)
print("Accuracy: ", round((nltk.classify.accuracy(classifier, testing_set) * 100), 2), "%")