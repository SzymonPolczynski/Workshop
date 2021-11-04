def pick_a_number():
    while True:
        try:
            player_number = int(input("Pick a number: "))
            break
        except ValueError:
            print("It's not a number!")
    return player_number


def pick_a_numbers():
    player_numbers = []
    while len(player_numbers) < 6:
        player_number = pick_a_number()
        if player_number not in player_numbers and player_number > 0 and player_number < 49:
            player_numbers.append(player_number)
        else:
            print("Wrong number!")
            pick_a_number()
    return player_numbers.sort()

def lotto_main():
    print(f"Your numbers are: {pick_a_numbers()}")



if __name__ == '__main__':
    lotto_main()
