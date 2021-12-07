from src.utils import exec_utils
from src.utils.aux_utils import progress
from random import randrange
from threading import Thread


def tweeting(count):
  while(True):
    print("-----------------------------------------------")
    choice = randrange(0, 1)
    if(choice < .7):
        content = exec_utils.get_random_phrase()
    else:
        content = exec_utils.get_random_verse()
    exec_utils.verify_tweet_existence(content)
    print_count_message(choice, count + 1, content)
    count += 1
    print("Sleeping... zZzZz")
    progress(100)
    exec_utils.register_tweet(content)
    print("Woke up!")


def start():
  count = 0
  tweet_thread = Thread(target=tweeting, args=(count,))
  tweet_thread.start()
  tweet_thread.join()
  

def print_count_message(choice, count, content):
  if(choice < .7):
    print(f"{count}: Tweeting about UID!")
    print("## Selected content:\n")
    print(content)
  else:
    print(f"{count}: Tweeting about lyrics!")
    print("## Selected content: \n")
    print(content)
  print("-----------------------------------------------")
