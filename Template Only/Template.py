import tweepy
import time

api_key = '1btNVewN1tQrWUVp35LU0TiC3'
api_secret = '0UULtTLvsNqq81GbKSgS8ba0qk2QaBHC3zviNC2N51fkfLNInY'
access_token = '1096377279712641027-yBSrQqbh37rjsI8J5UT2RJSiKbw2pP'
access_token_secret = 'Huyus3I71FCpxGQDOerEMPntqssj1eEX8H0BRVGpTkERE'
auth = tweepy.OAuthHandler(api_key, api_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

user = api.me()
print (user.name) #prints your name.
print (user.screen_name)
print (user.followers_count)

search = "zerotomastery"
numberOfTweets = 2

def limit_handle(cursor):
  while True:
    try:
      yield cursor.next()
    except tweepy.RateLimitError:
      time.sleep(1000)

#Be nice to your followers. Follow everyone!
for follower in limit_handle(tweepy.Cursor(api.followers).items()):
  if follower.name == 'Usernamehere':
    print(follower.name)
    follower.follow()


# Be a narcisist and love your own tweets. or retweet anything with a keyword!
for tweet in tweepy.Cursor(api.search, search).items(numberOfTweets):
    try:
        tweet.favorite()
        print('Retweeted the tweet')
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break


