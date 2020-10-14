import random
import sys
from time import sleep
words = ["hello", "cat", "dog", "summer", "school", "rocket", "lion", "eight", "madagascar", "synecdoche", "syzygy", "neptune", "goodbye", "what", "flower"]
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
hangman_word = random.choice(words)
word_guess = []
letter_storage = []
word_length = len(hangman_word)


def rules():
    for characters in hangman_word:
        word_guess.append("-")
    print("Length of the word is " + str(word_length) + ".")
    sleep(2)
    print("You have ten guesses.")
    sleep(2)
    print(word_guess)
    sleep(2)

def wordguess():
    while True:
        initial = input("Would you like to guess the word? yes or no?").lower()

        if initial == "yes":                  
            word_guess = input("Enter your guess.").lower()
            if word_guess == hangman_word:
                print("Congratulations!")
                sys.exit()
            else:
                print("Sorry, that's not the correct word.")
                sys.exit()
        elif initial == "no":
            print("Let's continue.")
            break
        else:
            print("Please enter in yes or no.")
            continue
            
def letterguess():
    number_of_guesses = 0
    while number_of_guesses <= 10:
        wordguess()
         
        letter_guess = input("Enter your letter guess.").lower()
        if letter_guess not in letters:
            print("Please enter in a letter (English alphabet).")
        elif letter_guess in letter_storage:
            print("You have already guessed this.")
        else:
            letter_storage.append(letter_guess)

        if letter_guess in hangman_word:
            print("Nice guess!")
            for x in range(0, word_length):
                if hangman_word[x] == letter_guess:
                    word_guess[x] = letter_guess
                    print(word_guess)
            if "-" not in word_guess:
                print("You have won!")
                break
        else:
            print("Incorrect guess. Try again.")
            number_of_guesses += 1
            if number_of_guesses == 10:
                print("You have lost. The word was " + hangman_word + ".")
                break

rules()
letterguess()
                        
    
