from game_data import data as d
import random


def check_answer(answer, celeb_a, celeb_b):
    a_followers = celeb_a["follower_count"]
    b_followers = celeb_b["follower_count"]

    result = a_followers if a_followers > b_followers else b_followers

    return answer == result


def high_low():
    game_over = False
    score = 0

    a = random.choice(d)
    b = random.choice(d)

    while not game_over:

        print(f'Compare A: {a["name"]}, a {a["description"]}, from {a["country"]}')
        print(f'Against B: {b["name"]}, a {b["description"]}, from {b["country"]}')

        answer = input("Who has the most followers? Type 'A' or 'B'\n").lower()

        if answer == 'a':
            answer = a["follower_count"]
        elif answer == 'b':
            answer = b["follower_count"]
        else:
            print('You have typed the wrong answer')
            game_over = True

        check = check_answer(answer, a, b)

        if check:
            score += 1
            a = b
            b = random.choice(d)
            print(f"You are right! Current score: {score}.")
        else:
            print(f"Sorry, that's wrong. Final score: {score}.")
            game_over = True


high_low()
