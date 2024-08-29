import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game = [rock, paper, scissors]
choice = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors'))

if choice >= 0 and choice <= 2:
    choice = game[choice]
    print('You chose:\n', choice)

    comp_choice = game[random.randint(0, 2)]
    print('Computer chose:\n', comp_choice)

    if choice == rock and comp_choice == scissors:
        print('You win')
    elif choice == rock and comp_choice == paper:
        print('You lose')
    elif choice == paper and comp_choice == rock:
        print('You win')
    elif choice == paper and comp_choice == scissors:
        print('You lose')
    elif choice == scissors and comp_choice == rock:
        print('You lose')
    elif choice == scissors and comp_choice == paper:
        print('You win')
    else:
        print('Draw')
else:
    print('You have typed an invalid number')
