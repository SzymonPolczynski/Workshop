import random


def pick_a_number():
    """ Get number form user
    Validate if input is a int"""
    while True:
        try:
            result = int(input("Guess the number: "))
            break
        except ValueError:
            print("It's not a number!")

    return result


def guess_the_number():
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