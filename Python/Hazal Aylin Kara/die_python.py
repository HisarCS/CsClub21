import random
""" min_die = 1
max_die = 6

def die_roll():
    roll_count = int(input("How many times would you like to roll the die?"))
    for i in range(roll_count):
        print(random.randint(min_die, max_die))

while True:
    die_roll() """


""" min_number = 1
max_number = 30
actual_number = random.randint(min_number, max_number)

def higher():
    print("Wrong. The real number is higher than your guess.")
    ask_again = int(input("Would you like to try again? Write 1 for yes."))
    if ask_again == 1:
        guess()
    else:
        print("Game over.")

def lower():
    print("Wrong. The real number is lower than your guess.")
    ask_again = int(input("Would you like to try again? Write 1 for yes."))
    if ask_again == 1:
        guess()
    else:
        print("Game over.")        

def guess():
    guess_number = int(input("Guess a number from 1-30."))
    if guess_number == actual_number:
        print("You got it right!")
    elif guess_number < actual_number:
        higher()
    elif guess_number > actual_number:
        lower()
        
while True:
    guess() """
    
    
