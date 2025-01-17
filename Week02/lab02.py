import random
def number_guessing_game():
    targetNumber = random.randint(1, 100)

    play = input("Do you want to play a number guessing game? (yes/no)").strip().lower

    attemps = 0
    max_attemps = 10

    while attemps < max_attemps:
        try:
            userGuess = int(("Enter your guess"))
            #attemps = + 1
            attemp += 1
            if userGuess < targetNumber:
                if (userGuess - targetNumber) <= 5:

                    print ("Too low ! You're very close! Try again.")
                else:
                    print("To low, try again.")
            elif userGuess > targetNumber:
                if abs(userGuess - targetNumber) <= 5:
                    print("Too high ! Try again.")
                else:
                    print(f"Congradulations! You've guesse it in {attemps} attemps.")

            return True
        except:
            print("")
    play = input()
    return True