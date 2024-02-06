import random
def guess_the_number():
    print("Hello! What is your name?")
    zagadka = random.randint(1, 20)
    count_guess = 0
    player_name = input()
    print(f"Well, {player_name}, I am thinking of a number between 1 and 20.\nTake a guess.")
    while True:
        guess = int(input())
    
    
        if guess == zagadka:
            print(f"Good job, {player_name}! You guessed my number in {count_guess} guesses!")
        elif guess > zagadka:
            print("Your guess is too more. \nTake a guess.")
            count_guess += 1
        elif guess < zagadka:
            print("Your guess is too low. \nTake a guess.")
            count_guess += 1
    

guess_the_number()