bids = {}

bid = True
while bid :
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n")
    if should_continue == "no":
        continue_bidding = False


def highest_bidder (bid_history):
    highest_bid = 0
    winner = ""
for bids in






