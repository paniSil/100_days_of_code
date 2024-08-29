import random


def card_deal():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    deal = random.choice(cards)
    return deal


def card_sum(card_list):
    hand_sum = sum(card_list)
    if len(card_list) == 2 and hand_sum == 21:
        return 0
    if hand_sum > 21 and 11 in card_list:
        card_list[card_list.index(11)] = 1
    return hand_sum


def compare(player_hand_sum, dealer_hand_sum):
    if player_hand_sum == dealer_hand_sum:
        print('Draw!')
    elif dealer_hand_sum == 0:
        print('Dealer has Black Jack! You lose')
    elif player_hand_sum == 0:
        print('You have Black Jack! You win!')
    elif player_hand_sum > 21:
        print('Bust!')
    elif dealer_hand_sum > 21:
        print('You win!')
    elif player_hand_sum > dealer_hand_sum:
        print('You win!')
    else:
        print('You lose!')


def play_game():
    player = []
    dealer = []
    is_game_over = False

    for card in range(2):
        player.append(card_deal())
        dealer.append(card_deal())

    while not is_game_over:

        player_sum = card_sum(player)
        dealer_sum = card_sum(dealer)

        print(f'Your cards: {player}, your score: {player_sum}')
        print(f'Dealer\'s first card {dealer[0]}')

        if dealer_sum == 0 or player_sum == 0 or player_sum > 21:
            is_game_over = True
        else:
            bet = input('One more card? Yes or no?\n')
            if bet.lower() == 'yes':
                player.append(card_deal())
                player_sum = card_sum(player)
            else:
                is_game_over = True

    while card_sum(dealer) < 17 and card_sum(dealer) != 0:
        dealer.append(card_deal())
        dealer_sum = card_sum(dealer)

    print(f'\nYour hand: {player} and your score: {player_sum}')
    print(f'Dealer hand: {dealer} and dealer\'s score: {dealer_sum}')
    compare(player_sum, dealer_sum)


while input('\nDo you want to play a game of Blackjack? Yes or no?\n').lower() == 'yes':
    play_game()
