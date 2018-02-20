"""
Name: Justin K. Pusztay
File name: twitter_analysis.py

This file looks at the text file with all the JSON code and finds the tweets
that have both Donald Trump and ice cream in it.
"""

import json
import pandas as pd
import matplotlib.pyplot as plt
import re

#The text document with the raw data
raw_data = 'twitDB.txt'


def jsonCreator(raw_data):
    """This function takes the raw data and makes a more Python readable 
    version."""
    tweets_data = []
    tweets_file = open(raw_data, "r")
    for line in tweets_file:
        try:
            tweet = json.loads(line)
            tweets_data.append(tweet)
        except:
            continue
    return tweets_data



def pandaData():
    """Creates the panda data frame, most used data structure in pandas 
    library."""
    tweets = pd.DataFrame()
    return tweets

"""
Some cool code that prints a bar graph with number of tweets in 3 most popular
languages found. 


tweets['lang'] = list(map(lambda tweet: tweet.get('lang',None), tweets_data))

tweets_by_lang = tweets['lang'].value_counts()
fig, ax = plt.subplots()
ax.tick_params(axis='x', labelsize=20)
ax.tick_params(axis='y', labelsize=15)
ax.set_xlabel('Languages', fontsize=15)
ax.set_ylabel('Number of tweets' , fontsize=15)
ax.set_title('Top 3 languages', fontsize=15, fontweight='bold')
tweets_by_lang[:3].plot(ax=ax, kind='bar', color='red')
"""

def word_finder(word, text):
    """Finds a tweet with a certain word\phrases in it."""
    word = word.lower()
    text = str(text).lower()
    match = re.search(word, text)
    if match:
        return True
    return False

def two_word_finder(word1,word2,text):
    """Finds a tweet with a two certain words\phrases in it."""
    word1 = word1.lower()
    word2 = word2.lower()
    text = str(text).lower()
    if word1 and word2 in text:
        return True #return text to see specific tweets
    return False

def main():
    print("The number of tweets collected from streaming: ", 
      len(jsonCreator(raw_data)))
    tweets = pandaData()
    #The line below adds the tweet to the panda data frame.
    tweets['text'] = list(map(lambda tweet: tweet.get('text',None), tweets_data))
    #These lines execute the word finder functions 
    tweets['trump'] = tweets['text'].apply(
        lambda tweet: word_finder('trump', tweet))
    tweets['ice cream'] = tweets['text'].apply(
        lambda tweet: word_finder('ice cream', tweet))

    print ("Number of tweets about ice cream: ",
       tweets['ice cream'].value_counts()[True])

    print ("Number of tweets about Trump: ",
           tweets['trump'].value_counts()[True])
    
    #Excutes two word finder function
    words = ['ice cream', 'trump']
    tweets_by_words = [tweets['ice cream'].value_counts()[True], 
                   tweets['trump'].value_counts()[True]]


    tweets['test'] = tweets['text'].apply
    (lambda tweet: two_word_finder('Donald Trump','ice cream', tweet))

    print("Number of tweets about Donald Trump and Ice Cream: ",
          tweets['ice cream'].value_counts()[True])

    #Uncomment to see text of tweets
    #See comment in two_word_finder() as well
    #lyst_of_tweets = list()
    #for x in tweets['test']:
        #if x != False:
            #lyst_of_tweets.append(x)

if __name__ == '__main__':
    main()

        
