import time

print("Think of a number from 0 to 1000 \nand I will guess it in max 10 trys!")
time.sleep(5)


def player_number():
    answers = ["too small", "too big", 'you win']
    while True:
        player_answer = input().lower()
        if player_answer in answers:
            break
        else:
            print("It's not correct answer\n Try: too small, too big or you win")
    return player_answer


def guessing_game_2():
    minimum = 0
    maximum = 1000
    player_answer = ""
    while player_answer != "you win":
        guess = int((maximum - minimum) // 2) + minimum
        print(f"I'm guessing: {guess}")
        player_answer = player_number()
        if player_answer == "too small":
            minimum = guess
        elif player_answer == "too big":
            maximum = guess
    print("Superior machine wins again!")


if __name__ == '__main__':
    guessing_game_2()
