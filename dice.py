import random

DICES = ("D3", "D4", "D6", "D8", "D10", "D12", "D20", "D100")


def rolling_dice(dice_spec):
    """Main function body checks if user input dice is in dice-set given
    Function also analise dice code checking for dice multiplyer and modifier
    Validates input for incorrect dice code"""
    for dice in DICES:
        if dice in dice_spec:
            try:
                multiply, modifier = dice_spec.split(dice)
            except ValueError:
                return "Wrong Input"
            dice_value = int(dice[1:])
            break
    else:
        return "Wrong Input"

    try:
        multiply = int(multiply) if multiply else 1
    except ValueError:
        return "Wrong Input"

    try:
        modifier = int(modifier) if modifier else 0
    except ValueError:
        return "Wrong Input"

    return sum([random.randint(1, dice_value) for _ in range(multiply)]) + modifier


if __name__ == '__main__':
    print(rolling_dice("D6"))
    print(rolling_dice("D16"))
    print(rolling_dice("2D20+5"))
    print(rolling_dice("2D12-2"))
    print(rolling_dice("K10+5"))
    print(rolling_dice("3D3+A"))
