from src.utils import exec_utils
from src.utils.aux_utils import progress
from random import randrange

def start():
  count = 0
  while(True):
    print("-----------------------------------------------")
    choice = randrange(0,1)
    if(choice < .7):
        content = exec_utils.get_random_phrase()
    else:
        content = exec_utils.get_random_verse()
    exec_utils.verify_tweet_existence(content)
    print_count_message(choice, count + 1, content)
    count += 1
    print("Sleeping... zZzZz")
    progress(10) #1800s = 42 times per day
    exec_utils.register_tweet(content)
    print("Woke up!")
      

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
