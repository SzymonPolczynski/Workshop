from random import randint


def pick_a_number():
    """ Get number form user
    Validate if input is an int"""
    while True:
        try:
            player_number = int(input("Pick a number: "))
            break
        except ValueError:
            print("It's not a number!")
    return player_number


def pick_a_numbers():
    """ Creating list of 6 numbers
    Validate if numbers are correct"""
    player_numbers = []
    while len(player_numbers) < 6:
        player_number = pick_a_number()
        if player_number not in player_numbers and 0 < player_number < 49:
            player_numbers.append(player_number)
        else:
            print("Wrong number!")
    player_numbers.sort()
    return player_numbers


def lotto_main():
    """ Main function
    Generating 6 number list
    Checking match with player numbers"""
    lotto_numbers = [randint(1, 49) for _ in range(6)]
    lotto_numbers.sort()
    player_numbers = pick_a_numbers()
    print(f"Your numbers: {player_numbers}")
    print(f"Drawn numbers: {lotto_numbers}")
    matched_numbers = []
    for number in player_numbers:
        if number in lotto_numbers:
            matched_numbers.append(number)
    if len(matched_numbers) >= 3:
        print(f"You scored {len(matched_numbers)} numbers. You won!")
    elif len(matched_numbers) == 2:
        print(f"You scored {len(matched_numbers)} numbers. You lost!")
    else:
        print(f"You scored {len(matched_numbers)} number. You lost!")


if __name__ == '__main__':
    lotto_main()
