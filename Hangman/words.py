import random

def load_words():
    with open("words.txt", 'r+') as file:
         mylist = [line.rstrip('\n').split(" ") for line in file]
    return mylist[0]

def choose_word():
    word_list = load_words()
    secret_word = random.choice(word_list)
    secret_word = secret_word.lower()

    return secret_word
print(choose_word())