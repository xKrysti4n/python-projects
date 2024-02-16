import os
from gavel import logo
end = True
highest_bid = 0
highest_bid_name = ""

bidders = []


def add_to_bidders(name,bid):
    new_bidder = {}
    new_bidder["name"] = name
    new_bidder["bid"] = bid
    bidders.append(new_bidder)


print(logo)

name = input("Name: ")
bid = int(input("Bid: " + "$"))
add_to_bidders(name,bid)


while end:
    os.system('cls')
    print(logo)
    name = input("Name: ")
    bid = int(input("Bid: " + "$"))
    answer = input("Is there any other user whot want to bid? (yes/no)").lower()
    if answer == "no": 
        end = False
    add_to_bidders(name,bid)
    os.system('cls')
    
for key in range(len(bidders)):
    find_bid = bidders[key]["bid"]
    if find_bid > highest_bid:
        highest_bid = find_bid
        highest_bid_name = bidders[key]["name"]

print(f'{highest_bid_name} won the auction. With ${highest_bid} bid!')