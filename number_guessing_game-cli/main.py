import random
from art import logo 
from os import system
play_again = True
player_choose = True
while play_again:
    system('cls')
    guess = random.randint(1,100)
    print(logo)
    print("Welcome in number guessing game!")

    print("I'm thinking the number between 1 to 100")

    difficulty = input("Choose difficulty (easy 10 attemps/hard 5 attemps): ").lower()

    if difficulty == "easy":
        attemps = 10
    elif difficulty == "hard":
        attemps = 5

    win = False
    while not win:
        print(f"You have {attemps} attemps")
        player_guess = int(input("Guess a number: "))
        if(attemps == 1):
            print("You lose, the number I was thinking of is " + str(guess))
            player_choose = input("Do you want to play again? (yes/no): ").lower()
            win = True
        elif player_guess > guess:
            print("Too high!")
            attemps-=1
        elif player_guess < guess:
            print("Too low")
            attemps-=1
        elif player_guess == guess:
            print("You won!")
            win = True
            player_choose = input("Do you want to play again? (yes/no): ").lower()
        else:
            print("Wrong Input")
        if player_choose == "yes":
            play_again = True
        elif player_choose == "no":
            play_again = False