"""
Name: Justin K. Pusztay
File name: twitter_stream.py

This files runs the twitter stream and stores data in text file.
"""


from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import time

#Codes not included for security reasons. Code will not run correctly!
access_token = "XXXXXXX"
access_token_secret = "XXXXXXXX"
consumer_key = "XXXXXXXXX"
consumer_secret = "XXXXXXXX"

class listener(StreamListener):
    """Creates a listener object."""
    def on_data(self,data):
        "Stores data in text file."""
        saveFile = open('twitDB.txt','a')
        saveFile.write(data)
        saveFile.write('\n')
        saveFile.close()
        return True

    def jsonCreator(self):
        "Creates JSON code to make useful for computer."""
        tweets_data = []
        tweets_file = open("twitDB.txt", "r")
        for line in tweets_file:
            try:
                tweet = json.loads(line)
                tweets_data.append(tweet)
            except:
                continue
        return tweets_data
        
    def on_error(self, status):
        """Prints the status fo the stream."""
        print(status)


def main():
    stream = listener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    twitterStream = Stream(auth,stream)
    twitterStream.filter(track=["trump","ice cream"])
            
if __name__ == '__main__':
    main()


