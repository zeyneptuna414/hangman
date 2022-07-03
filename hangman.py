
'''
This is the Hnagman Project
Author ADA
'''

from ast import Str
from ctypes.wintypes import HGLOBAL
from itertools import count
from multiprocessing.sharedctypes import copy
from operator import length_hint
from sys import displayhook
import time
import random
import copy

#Initial Steps to introduce the game to the players
print('\nWelcome to Hangman Game\n')
players_name = input('Enter your name to start the game: ')
print('Hello {}! Best of Luck!'.format(players_name))
time.sleep(2)
print('The game is about to start!\nLet\'s play Hangman!')
time.sleep(3)

#Defining the main function that initailizes the arguments
def main():
    global count
    global display
    global word
    global already_guessed
    global length  
    global play_game
    words_to_guess = ["january", "border", "image", "film", "promise",
    "kids", "lungs", "doll", "rhyme", "damage", "plants" ]
    word = random.choice(words_to_guess)
    length = len(word)
    count = 0
    display = '_' * length
    already_guessed = []
    play_game = ""  

#A loop to re-execute the game when the first round ends
def play_loop():
    global play_game
    play_game = input('Do you want to play again? y = yes, n = no \n')
    while play_game not in ['y', 'Y', 'n', 'N']:
        play_game = input('Do you want to play again? y = yes, n = no \n')
    if play_game == 'y':
        main()
    elif play_game == 'n':
        print('Thanks for playing! We expect you to back again!')
        exit()

def hangman():
    global count
    global display
    global word
    global already_guessed
    global play_game
    actual_word = copy.copy(word)
    limit = 5
    guess = input('This is the Hangman Word: ' + display + 'Enter your guess: \n')
    guess.strip()
    if len(guess.strip()) == 0 or len(guess.strip()) >= 2 or guess <= '9':
        print('Invalid Input, Try a letter\n')
        hangman()

    elif guess in word:
        already_guessed.extend([guess])
        index = word.find(guess)
        word = word[:index] + '_' + word[index + 1:]
        display = display[:index] + guess + display[index + 1:]
        print(display + '\n')

    elif guess in already_guessed:
        print('Try another letter.\n')

    else:
        count += 1
        if count == 1:
            time.sleep(1)
            print("   _____ \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print('Wrong guess.' + str(limit - count) + ' guesses remaining\n')
        
        elif count == 2:
            time.sleep(1)
            print("   _____ \n"
                  "  |     |\n"
                  "  |     |\n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print('Wrong guess.' + str(limit - count) + ' guesses remaining\n')

        elif count == 3:
            time.sleep(1)
            print("   _____ \n"
                  "  |     |\n"
                  "  |     |\n"
                  "  |     |\n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print('Wrong guess.' + str(limit - count) + ' guesses remaining\n')

        elif count == 4:
            time.sleep(1)
            print("   _____ \n"
                  "  |     |\n"
                  "  |     |\n"
                  "  |     O \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print('Wrong guess.' + str(limit - count) + ' guesses remaining\n')

        elif count == 5:
            time.sleep(1)
            print("   _____ \n"
                  "  |     |\n"
                  "  |     |\n"
                  "  |     O \n"
                  "  |    /|\  \n"
                  "  |    / \  \n"
                  "  |        \n"
                  "__|__\n")
            print('Wrong guess. You are hanged!!!\n')
            print('The word was:', actual_word)
            play_loop()

        
    if word == '_' * length:
        print('Congrats! You have guessed the word correctly!')
        play_loop()

    elif count != limit:
        hangman() #It makes it a loop. 
        #We didn't use any loop for the game before.
        #Count is a global variable. It is the same outside.

main()

hangman()











