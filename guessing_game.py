import random


def pick_a_number():
    """ Get number from user
    Validate if input is an int"""
    while True:
        try:
            player_number = int(input("Guess the number: "))
            break
        except ValueError:
            print("It's not a number!")

    return player_number


def guess_the_number():
    """ Main function
    compares player guesses with computer rolls"""
    comp_roll = random.randint(1, 100)
    player_guess = pick_a_number()
    while True:
        if player_guess > comp_roll:
            print("Too big!")
            player_guess = pick_a_number()
        elif player_guess < comp_roll:
            print("Too small!")
            player_guess = pick_a_number()
        else:
            print("You win!")
            break


if __name__ == '__main__':
    guess_the_number()
