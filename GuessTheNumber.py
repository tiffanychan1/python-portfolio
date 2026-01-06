# Guess the number in 10 tries or less

import random

def guess_the_number():
    
    print('You have 10 tries to guess the number 1-100. Good luck! \nType your first guess: ')
    
    number = random.randint(1,100)
    guesses = 0
    
    while guesses < 11:
        try:
            guess = int(input())
            guesses += 1
        
            if guess < number:
                print('Higher')
            elif guess > number:
                print('Lower')
            else:
                break
        except ValueError:
            print('Please only type numbers')
    
    if guess == number:
        print('You got the number in ' + str(guesses) + ' tries!')
    else:
        print('Sorry, you did not guess the number within 10 tries. The number was ' + str(number))
        
guess_the_number()
