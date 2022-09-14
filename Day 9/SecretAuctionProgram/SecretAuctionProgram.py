from art import logo

def highest_bidder(bid_record):
    highest_bid = 0
    for bid in bid_record:
        if highest_bid < bid_record[bid]:
            highest_bid = bid_record[bid]
    print(f"The highest bidder is {bid} with an amount of ${highest_bid}")


print(logo)

bid_prices = {}

bid_again = True
while bid_again:
    name = input("Enter your name: ")
    bid_price = int(input("What is your bid price? $"))
    bid_prices[name] = bid_price
    more_bids = input("Is there any other user who wants to bid? Yes or No: ")
    more_bids.lower()
    if more_bids == 'no':
        bid_again = False
    # else:
    # clear()

highest_bidder(bid_prices)
