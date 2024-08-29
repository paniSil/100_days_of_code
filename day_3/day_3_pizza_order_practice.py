print("Thank you for choosing Python Pizza Deliveries!")
size = input()  # What size pizza do you want? S, M, or L
add_pepperoni = input()  # Do you want pepperoni? Y or N
extra_cheese = input()  # Do you want extra cheese? Y or N
# 🚨 Don't change the code above 👆
# Write your code below this line 👇

sum = 0

if size == 'S':
    sum += 15
elif size == 'M':
    sum += 20
elif size == 'L':
    sum += 25

if add_pepperoni == 'Y' and size == 'S':
    sum += 2
elif add_pepperoni == 'Y' and (size == 'M' or size == 'L'):
    sum += 3

if extra_cheese == 'Y':
    sum += 1

print(f'Your final bill is: ${sum}.')
