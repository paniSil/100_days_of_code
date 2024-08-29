import random
from day_7_hangman_stages import stages


end_of_game = False
lives = 6
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

display = []
length = len(chosen_word)
for i in range(0, length):
    display += "_"

print(display)

while not end_of_game:

    guess = input(print('Guess a letter\n')).lower()

    position = 0
    for letter in chosen_word:
        if letter == guess:
            display[position] = letter
            position += 1
        else:
            position += 1

    if guess not in chosen_word:
        lives -= 1
        print(stages[lives])


    print(f"{''.join(display)}")

    if lives == 0:
        print('You lose')
        end_of_game = True

    if '_' not in display:
        print('You win')
        end_of_game = True
