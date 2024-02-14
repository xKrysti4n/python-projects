import numpy as np
import random
import stages
import os
list = np.loadtxt('words.txt',dtype='str')
password = random.choice(list)
lives = 5
blank_password = ["_"] * len(password)
end_of_game = False
lives = 6
os.system('cls')
print(stages.logo)

while not end_of_game:
    
    guess = input("Enter your guess: ").lower()
    os.system('cls')
    if guess not in password:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose! The word was " + password + "!")

    for i in range(len(password)):
        if guess == password[i]:
            blank_password[i] = guess
    print(' '.join(blank_password))

    if "_" not in blank_password:
        end_of_game = True
        print("You guessed the word! The word was" + password + "!")
    print(stages.stages[lives])