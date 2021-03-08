import random

print("Welcome to the Number gussing game!!")

number = random.randint(1, 9)
chance = 0

print("Guess a number from 1 to 9")

while chance < 5:
    guess = int(input("Enter your guess:- "))

    if(guess == number):
        print("You did find the number!!!")
        break

    elif(guess < number):
        print("Nah! It is higher number than this")

    else:
        print("Nope! It is lower number than this")

    chance += 1

    if not(chance < 5):
        print("you suck a lot in this game!!!")



