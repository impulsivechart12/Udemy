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

def run_scores(dealer_hand, player_hand):
    global dealer_score
    global player_score
    for card in dealer_hand:
        dealer_score += card
    for card in player_hand:
        player_score += card

def check_scores(player_score, dealer_score):
    if dealer_score == 21:


deal_cards(cards)
run_scores(dealer_hand, player_hand)

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

