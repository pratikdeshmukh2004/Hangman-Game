import string
from words import choose_word
from images import IMAGES

def get_hint(secret_word,letters_guessed):
    import random
    letter_not_guessed=[]
    for i in secret_word:
        if i not in letters_guessed:
            if i not in letter_not_guessed:
                letter_not_guessed.append(i)
    return random.choice(letter_not_guessed)

def ifValid(letter):
    if len(letter) != 1:
        return False

    if not letter.isalpha():
        return False
    return True

def is_word_guessed(secret_word, letters_guessed):
    if secret_word == get_guessed_word(secret_word, letters_guessed):
        return True

    return False

def get_guessed_word(secret_word, letters_guessed):

    index = 0
    guessed_word = ""
    while (index < len(secret_word)):
        if secret_word[index] in letters_guessed:
            guessed_word += secret_word[index]
        else:
            guessed_word += "_"
        index += 1
    
    return guessed_word


def get_available_letters(letters_guessed):
    import string
    letters_left = string.ascii_lowercase
    for i in letters_guessed:
        letters_left=letters_left.replace(i,"")

    return letters_left

def hangman(secret_word):

    print ("-------------Welcome to the game, Hangman!-------------")
    print ("I am thinking of a word that is " + str(len(secret_word)) + " letters long.")
    print ("")

    total_live=8
    remaining_live=8
    choice_choose_img=[0,1,2,3,4,5,6,7]

    print ("which level you want play this game?\n(a)	Easy \n(b)	Normal \n(c)	Hard")
    level=str(input("Enter your choice for level(a,b or c) "))
    if level=="b":
        total_live=remaining_live=6
        choice_choose_img=[1,2,3,4,6,7]
    elif level=="c":
        total_live=remaining_live=4
        choice_choose_img=[1,3,5,7]
    else:
        if level != "a":
            print ("your choice is wrong.\nGame starting in easy mode.")
    letters_guessed = []

    hint1=int(len(secret_word)/2)
    print (secret_word)
    while(remaining_live>0):
        available_letters = get_available_letters(letters_guessed)
        print ("\nAvailable letters: " + available_letters)

        guess = str(input("Please guess a letter(you have %s hints): "%hint1))
        letter = guess.lower()
        if letter == 'hint' and hint1>0:
            print ("\nYour hint for next word is "+get_hint(secret_word,letters_guessed))
            hint1+=1
            continue
        elif letter=="hint":
            print ("you have no hint")
            continue
        if ifValid(letter)==False:
            print ("invalid input")
            continue
        if letter in secret_word:
            letters_guessed.append(letter)
            print ("Good guess: " + get_guessed_word(secret_word, letters_guessed))
            print ("")

            if is_word_guessed(secret_word, letters_guessed):
                print (" * * Congratulations, you won! * * ")
                print ("")
                break
        else:
            print ("Oops! That letter is not in my word: " + get_guessed_word(secret_word, letters_guessed))
            letters_guessed.append(letter)
            print ("you loose please try again:")
            print (IMAGES[choice_choose_img[total_live-remaining_live]])
            remaining_live-=1
# Load the list of words into the variable wordlist
# So that it can be accessed from anywhere in the program
secret_word = choose_word()
hangman(secret_word)
