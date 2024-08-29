line1 = ["⬜️", "️⬜️", "️⬜️"]
line2 = ["⬜️", "⬜️", "️⬜️"]
line3 = ["⬜️️", "⬜️️", "⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input()  # Where do you want to put the treasure?
# 🚨 Don't change the code above 👆
# Write your code below this row 👇

letter = position[0]
if letter == 'A':
    letter = 0
elif letter == 'B':
    letter = 1
elif letter == 'C':
    letter = 2

number = position[1]

if number == '1':
    line1[letter] = 'X'
elif number == '2':
    line2[letter] = 'X'
elif number == '3':
    line3[letter] = 'X'

# Write your code above this row 👆
# 🚨 Don't change the code below 👇
print(f"{line1}\n{line2}\n{line3}")
