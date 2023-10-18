import os
from secret_auction_art import logo

bid_wars = {}
still_bidding = True

print(logo)

def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bid_wars:
        bid_amount = bid_wars[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}.")

while still_bidding:
    name = input("What is your name?\n")
    persons_bid = int(input("What's your bid?: $"))
    bid_wars[name] = persons_bid
    other_bids = input("Are there other bidders? 'Y' for Yes and 'N' for No\n").lower()

    if other_bids == 'n':
        still_bidding = False
    os.system('cls')

find_highest_bidder(bidding_record=bid_wars)