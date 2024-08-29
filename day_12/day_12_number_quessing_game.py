import random


def difficulty():
    diff = input("Choose a difficulty. Type 'easy' of 'hard':").lower()
    if diff == 'easy':
        lives = 10
    elif diff == 'hard':
        lives = 5
    return lives


def guess_game():
    number = random.randint(1, 100)

    print('Welcome to the Number Guessing Game!\n I\'m thinking of a number between 1 and 100.')

    lives = difficulty()

    while lives > 0:
        print(f'You have {lives} attempts remaining to guess the number')
        guess = int(input('Make a guess:'))

        if guess < number:
            lives -= 1
            print('Too low.')
            print('Guess again.')
        elif guess > number:
            lives -= 1
            print('Too high.')
            print('Guess again.')
        else:
            print(f'Correct! You win! The answer is {number}')
            break

    if lives == 0:
        print('You have run out of guesses, you lose.')


guess_game()
