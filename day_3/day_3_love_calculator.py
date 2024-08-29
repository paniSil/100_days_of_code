print("The Love Calculator is calculating your score...")
name1 = input()  # What is your name?
name2 = input()  # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇

name1 = name1.upper()
name2 = name2.upper()

score1 = 0
for i in name1:
    if i in 'TRUE':
        score1 += 1

for i in name2:
    if i in 'TRUE':
        score1 += 1

score2 = 0
for i in name1:
    if i in 'LOVE':
        score2 += 1

for i in name2:
    if i in 'LOVE':
        score2 += 1

love_score = int(str(score1) + str(score2))

if love_score < 10 and love_score > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif love_score > 40 and love_score < 50:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f'Your score is {love_score}')
