from src.utils import exec_utils
from src.utils.aux_utils import progress
from tweepy import API, OAuthHandler
from random import randint
from threading import Thread


def auth(API_KEY, API_SECRET_KEY, ACCESS_TOKEN, ACCESS_TOKEN_SECRET):
  try:
    auth = OAuthHandler(API_KEY, API_SECRET_KEY)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    return API(auth)
  except Exception:
    return None


def update_description(api, message):
  try:
    api.update_profile(description=message)
  except Exception:
    print("Profile's update failed..")


def print_count_message(choice, count, content):
  if(choice > 0):
    print(f"{count}: Tweeting about UID!")
    print("## Selected content:\n")
    print(content)
  else:
    print(f"{count}: Tweeting about lyrics!")
    print("## Selected content: \n")
    print(content)
  print("-----------------------------------------------")


def tweet(api, content):
  print("Tweeting content..")
  try:
    api.update_status(content)
    print("Preparing to sleep.. ")
  except Exception:
    print("Error! Tweeting failed..")


def tweeting_loop(api, count):
  while(True):
    print("-----------------------------------------------")
    choice = randint(0, 1)
    if(choice > 0):
        content = exec_utils.get_random_phrase()
    else:
        content = exec_utils.get_random_verse()
    exec_utils.verify_tweet_existence(content)
    print_count_message(choice, count + 1, content)
    try:
      tweet(api, content)
      count += 1
      exec_utils.register_tweet(content)
      print("Sleeping... zZzZz")
      progress(450)
      print("Woke up!")
    except Exception:
      print("Error!")


def start_bot(api, tweet_count):
  count = tweet_count
  tweeting_loop_thread = Thread(target=tweeting_loop, args=(api, count))
  print(">> Started tweeting!")
  tweeting_loop_thread.start()
  tweeting_loop_thread.join()


def user_info(user):
  try:
    print("Authentication -------------------------------")
    print("User:", f'{user.screen_name}')
    print("Favourites Count:", user.favourites_count)
    print("Followers Count:", user.followers_count)
    print("Tweet Account:", f'https://twitter.com/{user.screen_name}')
  except Exception:
    print("Error, authentication failed..")
