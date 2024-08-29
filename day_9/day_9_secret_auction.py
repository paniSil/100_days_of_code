from replit import clear
# HINT: You can call clear() to clear the output in the console.

is_run = True
all_bids = {}
while is_run:
    name = input('What is your name?\n')
    bid = int(input('Enter your bid price\n'))
    all_bids[name] = bid

    next_user = input('Is there another user? Yes or No')
    if next_user.lower() == 'yes':
        clear()
    elif next_user.lower() == 'no':
        clear()
        is_run = False
    else:
        clear()
        print('You have entered wrong answer')

bids = list(all_bids.values())
bidders = list(all_bids.keys())

max_bid = max(bids)
max_bidder = bidders[bids.index(max_bid)]

print(f'The max bid is {max_bid} and the winner is {max_bidder}')
