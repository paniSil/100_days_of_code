print('Welcome to the Tip Calculator\n')

total = int(input('Enter the bill sum\n'))
tip = input('Enter tip percentage\n')
people = int(input('How many guests are covering the bill\n'))

tip_adjustment = float('1.' + tip)
pay = (total/people)*tip_adjustment

print(f'Each person shoukd pay {"{:.2f}".format(pay)}$')
