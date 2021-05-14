import tweepy
import random
import utils
from time import sleep
import threading

def auth(API_KEY, API_SECRET_KEY, ACCESS_TOKEN, ACCESS_TOKEN_SECRET):
    auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    return tweepy.API(auth)

def tweet(api, message):
    print("Usings Twitter API..")
    api.update_status(message)
    print("Done!")

def update_description(api, message):
    api.update_profile(description=message)

def print_count_message(choice, count):
    if(choice>0):
        print(f"{count}: Tweet book excerpt!")
    else:
        print(f"{count}: Tweet lyrics!")

def start_bot(api, tweet_count):
    count = tweet_count
    while(True):
        print("-----------------------------------------------")
        choice = random.randint(0,1)
        if(choice > 0):
            content = utils.get_random_phrase()
        else:
            content = utils.get_random_verse()
        try:
            tweet_thread = threading.Thread(target=tweet, args=(api, content))
            tweet_thread.start()
            tweet_thread.join()
            count += 1
            print_count_message(choice, count)
        except tweepy.errors.TweepyException as e:
            print("Error!")
        print("Sleeping... zZzZz")
        utils.progress(1800) # 42 times per day
        print("Woke up!")
