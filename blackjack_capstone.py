from blackjack_art import logo
import random


print(logo)

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player_hand = []
dealer_hand = []
player_score = 0
dealer_score = 0
def deal_cards(card_list):
    player_hands = random.choices(cards, k=2)
    dealer_hands = random.choices(cards, k=2)
    for counter in range(0,2):
        player_hand.append(player_hands[counter])
        dealer_hand.append(dealer_hands[counter])
    print(f"You were dealt {player_hand}")
    print(f"The Dealer was dealt a {dealer_hand}")

def check_dealer(dealer_hand):
    global dealer_score
    for card in dealer_hand:
        dealer_score += card
    if dealer_score == 21:
        print("Dealer has BlackJack, you lose.")

deal_cards(cards)
check_dealer(dealer_hand)


# play_blackjack = True
#
# while play_blackjack:
#     to_play = input("Do you want to play blackjack? Type 'Y' for yes and 'N' for no: ").lower()
#     if to_play == 'y':
#         deal_cards(cards)
#         add_cards(player = player_hand, dealer = dealer_hand)
#     else:
#         play_blackjack = False
#         print("See you around the table another time.")

