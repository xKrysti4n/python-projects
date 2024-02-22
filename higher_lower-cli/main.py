import art
from game_data import data
import random
from os import system


ans_int = 0
final_score = 0

def new_vs():
    global final_score
    system('cls')
    first_data = random.choice(data)
    second_data = random.choice(data)

    follow_a = first_data["follower_count"]
    follow_b = first_data["follower_count"]

    while follow_a == follow_b:
        follow_b = random.choice(data)["follower_count"]

    print(art.logo)
    print(f"Compare A: {first_data['name']}, a {first_data['description']}, from {first_data['country']}")
    print(art.vs)
    print(f"Against B: {second_data['name']}, a {second_data['description']}, from {second_data['country']}")

    answer = input("Who has more followers? Type 'A' or 'B': ").upper()

    if answer == "A" and follow_a > follow_b:
        final_score += 10
        print(f"You guessed! Your score: {final_score}")
        input('Press <ENTER> to continue')

    elif answer == "B" and follow_b > follow_a:
        final_score += 10
        print(f"You guessed! Your score: {final_score}")
        input('Press <ENTER> to continue')

    else:
        print(f"You did not guess! Your score: {final_score}")
        input('Press <ENTER> to continue')


for _ in range(5):
    new_vs()

system('cls')
print(f"Your final score: {final_score}")