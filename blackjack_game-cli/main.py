import random
from art import logo

cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
user_cards = []
computer_cards = []

def deal_card():
    return random.choice(cards)

for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def calculate_winner(user_score, computer_score):
    if user_score == computer_score:
        return "It's a draw"
    elif computer_score == 0:
        return "You lose, opponent has Blackjack"
    elif user_score == 0:
        return "You win with a Blackjack"
    elif user_score > 21:
        return "You went over. You lose"
    elif computer_score > 21:
        return "Opponent went over. You win"
    elif user_score > computer_score:
        return "You win"
    else:
        return "You lose"

user_score = calculate_score(user_cards)
computer_score =  calculate_score(computer_cards)

print(logo)
print(f"Your cards: {user_cards}, current score: {user_score}")
print(f"Computer's first card: {computer_cards[0]}")

if user_score == 0 or computer_score == 0 or user_score > 21:
    print(calculate_winner(user_score, computer_score))
else:
    user_should_deal = True
    while user_should_deal:
        user_deal = input("Type 'y' to get another card, type 'n' to pass: ")
        if user_deal == "y":
            user_cards.append(deal_card())
            user_score = calculate_score(user_cards)
            print(f"Your cards: {user_cards}, current score: {user_score}")
            print(f"Computer's first card: {computer_cards[0]}")
            if user_score > 21:
                user_should_deal = False
                print(calculate_winner(user_score, computer_score))
        else:
            user_should_deal = False

computer_should_deal = True
while computer_should_deal and user_score <= 21:
    if computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)
    else:
        computer_should_deal = False

print(f"Your final hand: {user_cards}, final score: {user_score}")
print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
print(calculate_winner(user_score, computer_score))
