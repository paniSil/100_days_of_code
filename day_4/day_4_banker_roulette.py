# You are working in a team of developers.
# Another developer has written the code to import the names in the inputs
# You can run the code to see what this names list looks like.
# Then change the names in the input to see how it imports the names.
# print(names)
# 🚨 Remember to remove the print statement above when you submit.
import random

name_count = len(names)
winning_num = random.randint(0, name_count-1)
winner = names[winning_num]
print(f'{winner} is going to buy the meal today!')
