import tweepy
import random
from time import sleep
import os

def get_random_phrase(file):
    f = open(file, "r", encoding="utf8")
    phrases = f.read().split(".")
    f.close()
    phrase = ""
    while(len(phrase) == 0 or len(phrase) > 280):
        phrase = random.choice(phrases) + "."
    return phrase

def get_random_verse():
    albuns = os.listdir('./lyrics')
    path = './lyrics/' + random.choice(albuns)
    track = random.choice(os.listdir(path))
    final_path = path + '/' + track
    f = open(final_path, "r", encoding="utf8")
    verses = f.read().split("-")
    f.close()
    verse = random.choice(verses)
    # verse += "\n" + "Compositor: Sebastião Maia" 
    return verse


def auth(API_KEY, API_SECRET_KEY, ACCESS_TOKEN, ACCESS_TOKEN_SECRET):
    auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    return tweepy.API(auth)

def tweet(api, message):
    api.update_status(message)

def update_description(api, message):
    api.update_profile(description=message)

token = open('tokens.txt','r').read().splitlines()

API_KEY             = token[0]
API_SECRET_KEY      = token[1]
ACCESS_TOKEN        = token[2]
ACCESS_TOKEN_SECRET = token[3]

api = auth(API_KEY, API_SECRET_KEY, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
count = 0
while(True):
    choice = random.randint(0,1)
    if(choice > 0):
        content = get_random_phrase("./books/universo_em_desencanto_vol152.txt")
    else:
        content = get_random_verse()
    tweet(api, content)
    count += 1
    print(f"Tweet number {count}!")
    print("Sleeping... zzz")
    sleep(300)
    print("Woke up!")
