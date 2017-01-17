"""
Extracts various information about New Year's Resolutions 
from a twitter data feed and outputs to text file to be used
for data visualization
"""

import sys
import json

def buildTweets(tweet_file):
"""
Converts output from Twitter Streaming API into list of dictionaries

Parameters
----------
tweet_file: file object
        text file containing output from Twitter Streaming API

Returns
--------
list
        contains dictionary for each tweet

"""        
    tweets = []
    
    for line in tweet_file:
        jsn = json.loads(line)
        tweet = jsn
        tweets.append(tweet)

    tweet_file.seek(0)
    return tweets

def main():
	tweet_file = open(sys.argv[1])

        tweets = buildTweets(tweet_file)
        for tweet in tweets:
                
                location = tweet['user']['location']
                if location == None:
                        continue
                location = location.split()
                
                #print(tweet['user']['location'])
                print(location)


if __name__ == '__main__':
    main()
