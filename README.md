# SentimentAnalyzer_NLTK
A sentiment analyzer based on Yelp reviews built using NLTK, uses a Naive Bayes classifier and gets 60~65% accuracy

## Sentiment Analyzer

### Purpose

The purpose of this program is to classify text according to sentiment either positive or negative

### Data Set

The dataset that I used is the free review data that is provided by Yelp which can be found here: https://www.yelp.com/dataset

This dataset is an enormous file so you are going to need a special filer viewer in order to open it such as the one that can be found here: https://web.archive.org/web/20140908181354fw_/http://swiftgear.com/ltfviewer/features.html

I moved the first 10,000 reviews into a JSON file that I uploaded to this reprository as well

### Cleaning

This dataset is relatively clean, but it is not properly formatted as a JSON.  The format.py file will take care of this by adding commas and other formatting

### Methodology

The first thing we do is create a list of tuples that contain the a list of tokens and the sentiment of the review.  Four and five star reviews are considered positive reviews and one, two and three star reviews are considered negative reviews.  The tokens are normalized to lower case, punctuation is removed, and stop words are removed.

There are many more positive reviews than negative, so we create a list with an even number of each and then shuffle it for normalization.

Next we create a list of all the words present in the document and order it in terms of frequency.  We use a "bag of words" model where the features are the presence or absence of the most common 3000 words in all reviews.

We then use a Naive Bayes Classifier and train against 70% of the reviews and use 30% of the reviews for testing and check the accuracy.

### Accuracy

We typically get around 60~65% accuracy with this model as you can see in the image below.

![Output](https://github.com/ForTheGold/SentimentAnalyzer_NLTK/blob/main/Resources/Output.png)

## Technologies

* Python
* NLTK
* Machine Learning - Naive Bayes Model
