"""
Extracts various information about New Year's Resolutions 
from a twitter data feed and outputs to text file to be used
for data visualization
"""

import sys
import json

def buildTweets(tweet_file):
    """
    Converts json output from Twitter Streaming API into list of json dictionaries

    Parameters
    ----------
    tweet_file: file object
            text file containing output from Twitter Streaming API

    Returns
    --------
    list
            contains json dictionary for each tweet

    """        
    tweets = []
    #x = 0
    for line in tweet_file:
        #if x == 5000:
#            return tweets
        jsn = json.loads(line)
        tweet = jsn
        tweets.append(tweet)
#        x += 1

    tweet_file.seek(0)
    return tweets

def buildStateCount(tweets):
    """
    Counts the number of tweets per state in the U.S. and writes to file

    Parameters
    ----------
    tweets: list
            list of json dictionaries each representing a tweet
            
    outFile: file object
             file to be written to
             
    """

    states = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming''South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'}
    
    stateCount = {
        'AL': 0,
        'AK': 0,
        'AZ': 0,
        'AR': 0,
        'CA': 0,
        'CO': 0,
        'CT': 0,
        'DE': 0,
        'FL': 0,
        'GA': 0,
        'HI': 0,
        'ID': 0,
        'IL': 0,
        'IN': 0,
        'IA': 0,
        'KS': 0,
        'KY': 0,
        'LA': 0,
        'ME': 0,
        'MT': 0,
        'NE': 0,
        'NV': 0,
        'NH': 0,
        'NJ': 0,
        'NM': 0,
        'NY': 0,
        'NC': 0,
        'ND': 0,
        'OH': 0,
        'OK': 0,
        'OR': 0,
        'MD': 0,
        'MA': 0,
        'MI': 0,
        'MN': 0,
        'MS': 0,
        'MO': 0,
        'PA': 0,
        'RI': 0,
        'SC': 0,
        'SD': 0,
        'TN': 0,
        'TX': 0,
        'UT': 0,
        'VT': 0,
        'VA': 0,
        'WA': 0,
        'WV': 0,
        'WI': 0,
        'WY': 0}

    
    for tweet in tweets:
            
        location = tweet['user']['location']
        if location == None:
                continue
        location = location.split()

        #count the number of tweets per state
        for word in location:
            for key in states:
                if word == key or word == states[key]:
                    stateCount[key] += 1


    file = open('results.txt', 'a')
    file.write('Number of Tweets per State\n')
    for state in stateCount:
        file.write(state + ', ' + str(stateCount[state]) + '\n')
    
    file.write('\n')
    file.close()
    

def main():
    tweet_file = open(sys.argv[1])

    tweets = buildTweets(tweet_file)

    buildStateCount(tweets)


if __name__ == '__main__':
    main()
