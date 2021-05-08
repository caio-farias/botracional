import os
import random

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
