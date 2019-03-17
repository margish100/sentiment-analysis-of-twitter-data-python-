import pandas as pd
import numpy as np
import re
import twitter
import tweepy
import matplotlib
import matplotlib.pyplot as plt
import nltk
from nltk.corpus import stopwords
import random
from nltk.classify.scikitlearn import SklearnClassifier
from sklearn.naive_bayes import MultinomialNB,BernoulliNB
from sklearn.linear_model import LogisticRegression,SGDClassifier
from sklearn.utils import shuffle
import string

#matplotlib.get_backend()
#metadata = pd.read_csv("c:/users/lenovo/desktop/gender-classifier.csv",encoding='latin1')

#metadata.head(2)
#metadata.columns

def find_features(top_words, text):
    feature = {}
    for word in top_words:
        feature[word] = word in text.lower()
    return feature

df = pd.read_csv("C:\\Users\\Deep Ankur\\Desktop\\Student\\adittwitter\\genderanaylusis\\gender-classifier.csv",encoding='latin1')
df.head(10)

print (df.head(10))



all_descriptions = df['description']
all_tweets = df['text']
all_genders = df['gender']
all_gender_confidence = df['gender:confidence']
description_tweet_gender = []

bag_of_words = []
c = 0  # for the index of the row
stop = stopwords.words('english')
for tweet in all_tweets:
    description = all_descriptions[c]
    gender = all_genders[c]
    gender_confidence = all_gender_confidence[c]
    
    # remove the rows which has an empty tweet and description
    # remove the rows with unknown or empty gender
    # remove the rows which have gender:confidence < 80%
    if (str(tweet) == 'nan' and str(description) == 'nan') or str(gender) == 'nan' or str(gender) == 'unknown' or float(gender_confidence) < 0.8:
        c+=1
        continue
    
    if str(tweet) == 'nan':
        tweet = ''
    if str(description) == 'nan':
        description = ''
    
    # removal of punctuations
    for punct in string.punctuation:
        if punct in tweet:
            tweet = tweet.replace(punct, " ")
        if punct in description:
            description = description.replace(punct, " ")
            
    # adding the word to the bag except stopwords
    for word in tweet.split():
        if word.isalpha() and word.lower() not in stop:
            bag_of_words.append(word.lower())
    for word in description.split():
        if word.isalpha() and word.lower() not in stop:
            bag_of_words.append(word.lower())
    
    # using tweet and description for classification
    description_tweet_gender.append((tweet+" "+description , gender))
    c += 1
print("***********BAG_OF_WORDS***************")
print(len(bag_of_words))
print("*******************Descryption_tweet_gender*****************")
print(len(description_tweet_gender))

#getting features in bag of words

bag_of_words = nltk.FreqDist(bag_of_words)
top_words = []
for word in bag_of_words.most_common(4000):
    top_words.append(word[0])

top_words[:10]

print(top_words[:10])

#creating feature set

feature_set = [(find_features(top_words, text), gender) for (text, gender) in description_tweet_gender]
training_set = feature_set[:int(len(feature_set)*4/5)]
testing_set = feature_set[int(len(feature_set)*4/5):]

print("Length of feature set", len(feature_set))
print("Length of training set", len(training_set))
print("Length of testing set", len(testing_set))

#using Naive bayes for classification of tweets

NB_classifier = nltk.NaiveBayesClassifier.train(training_set)
accuracy = nltk.classify.accuracy(NB_classifier, testing_set)*100
print("Naive Bayes Classifier accuracy =", accuracy)
NB_classifier.show_most_informative_features(20)

#multimonial bayes classifier

MNB_classifier = SklearnClassifier(MultinomialNB())
MNB_classifier.train(training_set)
accuracy = nltk.classify.accuracy(MNB_classifier, testing_set)*100
print("Multinomial Naive Bayes Classifier accuracy =", (accuracy))

# creating a logistic regression classifier
LogisticRegression_classifier = SklearnClassifier(LogisticRegression())
LogisticRegression_classifier.train(training_set)
accuracy = nltk.classify.accuracy(LogisticRegression_classifier, testing_set)*100
print("Logistic Regression classifier accuracy =", accuracy)

description = "Programming with Python, Java and Android with little knowledge in web development. its good to be an Engineering student for now. Huge fan of Comics."
text = "Platform independent languages is like \" You can't C me\"."
features = find_features(top_words, description+" "+text)
print("*****NB classifier result******")
print(NB_classifier.classify(features))
print("*****Multimonial NB results********")
print(MNB_classifier.classify(features))
print("**********Logistic Regression_ Results***********")
print(LogisticRegression_classifier.classify(features))
