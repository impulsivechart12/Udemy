from blackjack_art import logo
import random

print(logo)

def deal_card():
    """Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    """Checks if player or dealer has 21. Also checks if hand is over 21 with and Ace, replaces
    Ace value of 11 to a 1"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(player_score, dealer_score):
    if player_score == dealer_score:
        return "Draw"
    elif dealer_score == 0:
        return "You lose, the dealer has a blackjack."
    elif dealer_score == 0:
        return "You win, you have a blackjack."
    elif player_score > 21:
        return "You busted, you lose."
    elif dealer_score > 21:
        return "The dealer busted, you win."
    else:
        return "You lose."

def play_game():
    print(logo)
    player_hand = []
    dealer_hand = []
    game_over = False
    for _ in range(2):
        player_hand.append(deal_card())
        dealer_hand.append(deal_card())

    while not game_over:
        player_score = calculate_score(player_hand)
        dealer_score = calculate_score(dealer_hand)
        print(f"Your cards are {player_hand}, and your score is {player_score}")
        print(f"Dealer cards are {dealer_hand[0]}")

        if player_score == 0 or dealer_score == 0 or player_score > 21:
            game_over = True
        else:
            player_choice = input("Type 'y' to hit, type 'n' to stay.\n").lower()
            if player_choice == "y":
                player_hand.append(deal_card())
            else:
                game_over = True

    while dealer_score !=0 and dealer_score < 17:
        dealer_hand.append(deal_card())
        dealer_score = calculate_score(dealer_hand)

    print(f"Your final hand: {player_hand}, final score: {player_score}")
    print(f"Dealers final hand: {dealer_hand}, final score: {dealer_score}")
    print(compare(player_score, dealer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n':") == "y":
    play_game()