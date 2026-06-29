from random import randint
for x in range(0,6) :
    guess = int(input("Guess a number between 0 to 5: "))
    rannumber = randint(0,5)
    if guess == rannumber :
        print("Congratulations! You guessed the number correctly.")
    else :
        print("Sorry! Your guess was incorrect")
        print(" The correct number was", rannumber)