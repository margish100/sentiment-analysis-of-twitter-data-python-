import pandas as pd
import numpy as np
import re
import twitter
import tweepy
import string
import matplotlib
import matplotlib.pyplot as plt
import nltk
from nltk.corpus import stopwords


matplotlib.get_backend()
metadata = pd.read_csv("C:\\Users\\Deep Ankur\\Desktop\\Student\\adittwitter\\genderanaylusis\\gender-classifier.csv",encoding='latin1')

metadata.head(2)
metadata.columns

data = pd.read_csv("C:\\Users\\Deep Ankur\\Desktop\\Student\\adittwitter\\genderanaylusis\\gender-classifier.csv",usecols= [0,5,19,17,21,10,11],encoding='latin1')
data.head(5)

print (data.head(5))

def cleaning(s):
    s = str(s)
    s = s.lower()
    s = re.sub('\s\W',' ',s)
    s = re.sub('\W,\s',' ',s)
    s = re.sub(r'[^\w]', ' ', s)
    s = re.sub("\d+", "", s)
    s = re.sub('\s+',' ',s)
    s = re.sub('[!@#$_]', '', s)
    s = s.replace("co","")
    s = s.replace("https","")
    s = s.replace(",","")
    s = s.replace("[\w*"," ")
    return s

data['Tweets'] = [cleaning(s) for s in data['text']]
data['Description'] = [cleaning(s) for s in data['description']]

from nltk.corpus import stopwords
nltk.download('stopwords')
stop = set(stopwords.words('english'))
data['Tweets'] = data['Tweets'].str.lower().str.split()
data['Tweets'] = data['Tweets'].apply(lambda x : [item for item in x if item not in stop])

data.head(5)

data.gender.value_counts()
print("***********gender value count***************")
print (data.gender.value_counts())

Male = data[data['gender'] == 'male']
Female = data[data['gender'] == 'female']
Brand = data[data['gender'] == 'brand']
Male_Words = pd.Series(' '.join(Male['Tweets'].astype(str)).lower().split(" ")).value_counts()[:20]
Female_Words = pd.Series(' '.join(Female['Tweets'].astype(str)).lower().split(" ")).value_counts()[:20]
Brand_words = pd.Series(' '.join(Brand['Tweets'].astype(str)).lower().split(" ")).value_counts()[:10]

Female_Words
print("*****************Female_Words*************")
print(Female_Words)

Female_Words.plot(kind='bar',stacked=True, colormap='OrRd_r')
plt.title('Female Words Count')
plt.show()


print("*********Male_words********")
print (Male_Words)

Male_Words.plot(kind='bar',stacked=True, colormap='plasma')
#plot.show()
plt.title('Males words Count')
plt.show()

print("*********Brand_words********")
print (Brand_words)
xx=len(Male_Words)
yy=len(Female_Words)
print (xx)
print (yy)
Brand_words.plot(kind='bar',stacked=True, colormap='plasma')
#plot.show()
plt.title('Brandwords Count')
plt.show()


multiple_bars = plt.figure()

x = [Male_Words,
     Female_Words,
     Brand_words]


y = [4, 9, 2]
z=[1,2,3]
k=[11,12,13]

ax = plt.subplot(111)
ax.bar(x-0.2, y,width=0.2,color='b',align='center')
ax.bar(x, z,width=0.2,color='g',align='center')
ax.bar(x+0.2, k,width=0.2,color='r',align='center')
ax.xaxis_date()

plt.show()

plot_url = plt.plot_mpl(multiple_bars, filename='mpl-multiple-bars')