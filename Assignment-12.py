# Assignment-12
import tweepy

# question-1 :
# Access Token : The Access Token is a credential that can be used by an application to access an API.
#Its purpose is to inform the API that the bearer of this token has been authorized to access the API
# and perform specific actions (as specified by the scope that has been granted).Access Tokens are
# typically obtained in order to access user-owned resources. For example, a Calendar application needs
# access to a Calendar API in the cloud in order to read the user's scheduled events and create new events.


#question-2 :
# Domain Name                     ip address
# www.google.com                  216.58.217.132
# www.facebook.com                31.13.72.36


# question-3 :
consumer_key = "..................................."
consumer_secret = "................................"
access_key = "....................................."
access_secret = ".................................."

# function to extract tweets :
def get_tweets(username):
    auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
    auth.set_access_token(access_key,access_secret)
    api = tweepy.API(auth)

    number_of_tweets = 200
    tweets = api.user_timeline(screen_name=username)
    tmp = []
    tweets_for_csv = [tweet.text for tweet in tweets]
    for j in tweets_for_csv:
        tmp.append(j)
    print(tmp)

print(get_tweets("...name..."))

# question-4 :

# Library : A Library is a chunk of code that you can call from your own code, to help you do things more quickly/easily.
# For example, a Bitmap Processing library will provide facilities for loading and manipulating bitmap images, saving you
# having to write all that code for yourself. Typically a library will only offer one area of functionality (processing
# images or operating on zip files) e.g., NumPy

# API : An API (application programming interface) is a term meaning the functions/methods in a library that you can call
# to ask it to do things for you - the interface to the library.
