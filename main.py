import tweepy
import random
from time import sleep
import os

def get_random_phrase():
    books = os.listdir('./books')
    path = './books/' + random.choice(books)
    f = open(path, "r", encoding="utf8")
    phrases = f.read().split(".")
    f.close()
    phrase = ""
    while(len(phrase) == 0 or len(phrase) > 280):
        phrase = random.choice(phrases)
    return phrase

def get_random_verse():
    albuns = os.listdir('./lyrics')
    path = './lyrics/' + random.choice(albuns)
    track = random.choice(os.listdir(path))
    final_path = path + '/' + track
    f = open(final_path, "r", encoding="utf8")
    verses = f.read().split("-")
    f.close()
    verse = ""
    while(len(verse) == 0 or len(verse) > 280):
        verse = random.choice(verses)
    return verse


def auth(API_KEY, API_SECRET_KEY, ACCESS_TOKEN, ACCESS_TOKEN_SECRET):
    auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    return tweepy.API(auth)

def tweet(api, message):
    api.update_status(message)

def update_description(api, message):
    api.update_profile(description=message)

def start_bot(api, tweet_count):
    count = tweet_count
    while(True):
        print("-----------------------------------------------")
        choice = random.randint(0,1)
        if(choice > 0):
            content = get_random_phrase()
        else:
            content = get_random_verse()
        print("Using Twitter API...")
        tweet(api, content)
        print("Done...")
        count += 1
        if(choice>0):
            print(f"{count}: Tweet book excerpt!")
        else:
            print(f"{count}: Tweet lyrics!")
        print("Sleeping... zZzZz")
        sleep(1200)
        print("Woke up!")

token = open('tokens.txt','r').read().splitlines()

API_KEY             = token[0]
API_SECRET_KEY      = token[1]
ACCESS_TOKEN        = token[2]
ACCESS_TOKEN_SECRET = token[3]

api = auth(API_KEY, API_SECRET_KEY, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
tweet_count = len(api.home_timeline())
start_bot(api, tweet_count)