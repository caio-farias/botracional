from os import listdir
from random import randint, choice
from datetime import datetime

def increment_repeated_tweets(file='repeated_tries_count.txt'):
  count = open(f'../logs/{file}','r').read()
  count = int(count)
  f = open(f'../logs/{file}','w', encoding='utf-8')
  f.write(str(count+1)) 
  f.close()

def verify_tweet_existence(content):
  content = content.strip().replace(' ', '').replace('\n', '')
  day = datetime.now().weekday() + 1 
  tweets_content = open(f'../logs/{day}.txt','r').read().split('#')
  if(content not in tweets_content):
    return
  increment_repeated_tweets()
  print(">>> Generating new content..")
  while(content in tweets_content):
    choice = randint(0,1)
    if(choice > 0):
        content = get_random_phrase()
    else:
        content = get_random_verse()

def register_tweet(content):
  content = content.strip().replace(' ', '').replace('\n', '')
  day = datetime.now().weekday() + 1
  log = open(f'../logs/{day}.txt', 'r', encoding='utf-8').read()
  f = open(f'../logs/{day}.txt','w', encoding='utf-8')
  f.write(log + content + '#') 
  f.close()

def get_random_phrase():
  books = listdir('../content_collection/books')
  path = '../content_collection/books/' + choice(books)
  f = open(path, "r", encoding="utf8")
  phrases = f.read().split(".")
  f.close()
  phrase = ""
  while(len(phrase) == 0 or len(phrase) > 280):
    phrase = choice(phrases)
  return phrase

def get_random_verse():
  albuns = listdir('../content_collection/lyrics')
  path = '../content_collection/lyrics/' + choice(albuns)
  track = choice(listdir(path))
  final_path = path + '/' + track
  f = open(final_path, "r", encoding="utf8")
  verses = f.read().split("-")
  f.close()
  verse = ""
  while(len(verse) == 0 or len(verse) > 280):
    verse = choice(verses)
  return verse
