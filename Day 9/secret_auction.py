from art import logo

print(logo)
print("Welcome to the secret auction program.")

def highest_bidder(bidding_record):
    highest_bid=0
    winner=''
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount>highest_bid:
            highest_bid=bid_amount
            winner = bidder
    print(f"The winner of this bid is {winner} with a bid of {highest_bid}")




bids={}
auction = False
while not auction :
    name=input("What is your name? :")
    price=int(input("What is your bid?: $"))
    bids [name] = price
    other_bidders=input("Are there any other bidders? Types 'yes' or 'no'")
    if other_bidders == "yes":
        auction = False
        print("\n"*20)
    elif other_bidders == "no":
        auction = True
        highest_bidder(bids)
