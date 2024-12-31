import random

def num_guess():
    list = [i for i in range(1, 101)]
    bot = random.choice(list)
    while True:
        try:
            user = int(input("Pick a random number from 1 to 100: "))
            if user < 1 or user > 100:
                raise OverflowError("Enter a valid number between 1 and 100!")
            elif user == bot:
                print(f"Bot choice: {bot}")
                print("Your choice matches the bot's choice, so you win.")
                break
            elif user > bot:
                print("The number chosen by you is greater than the bot's choice.")
            elif user < bot:
                print("The number chosen by you is smaller than the bot's choice.")
        except ValueError:
            print("Invalid input! Please enter a number.")
        except OverflowError as e:
            print(e)

num_guess()