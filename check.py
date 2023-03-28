import tweepy
import configparser
import pandas as pd


api_key = "ltZgbnYHzAQf1T7VcaNrKzDqL"
api_key_secret = "8kYGjkQfg2z5DBHi9s5I4JtnKP9EyITTrjdbIodashf8MCljGh"

access_token = "768892675508543488-euz5fkGHhBqySdQEOJbU6hV5U4kxPzu"
access_token_secret = "uMuoxwL5y49828Lmm3CjIo3G7fWazwxswA6sauWd7hABW"

bearer_token = "AAAAAAAAAAAAAAAAAAAAAIT5JgEAAAAAZ%2FaXxFBn0%2BbuKHsCcZlXfMrcFVs%3DHEoPjM3Ls16udIAkmSe32awfNaVcSoRyP7rzxZtJxwS6fHhSQq"

# read configs
config = configparser.ConfigParser()
config.read('config.ini')

# api_key = config['twitter']['api_key']
# api_key_secret = config['twitter']['api_key_secret']

# access_token = config['twitter']['access_token']
# access_token_secret = config['twitter']['access_token_secret']

print(api_key)
# authentication
auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

class Listener(tweepy.Stream):

    tweets = []
    limit = 40

    def on_status(self, status):
        self.tweets.append(status)
        print(status.user.screen_name + ": " + status.text)

        if len(self.tweets) == self.limit:
            self.disconnect()

stream_tweet = Listener(api_key, api_key_secret, access_token, access_token_secret)

keywords = ["python"]
def check_stream(i):
    stream_tweet.filter(track=keywords)

def start(args):
    print('algorithm started streaming')
    # input = args['input'][0]
    stream_tweet.filter(track=keywords)
    return args['input'][0]
