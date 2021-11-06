from flask import Flask, request


app = Flask(__name__)


START = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Guessing Game</title>
</head>
<body>
<h1>Think of a number between 0 and 1000</h1>
<form action="" method="POST">
    <input type="hidden" name="min" value="{}"></input>
    <input type="hidden" name="max" value="{}"></input>
    <input type="submit" value="OK">
</form>
</body>
</html>
"""


GUESSING = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Guessing Game</title>
</head>
<body>
<h1>It is number {guess}</h1>
<form action="" method="POST">
    <input type="submit" name="player_answer" value="too big">
    <input type="submit" name="player_answer" value="too small">
    <input type="submit" name="player_answer" value="you won">
    <input type="hidden" name="min" value="{min}">
    <input type="hidden" name="max" value="{max}">
    <input type="hidden" name="guess" value="{guess}">
</form>
</body>
</html>
"""


WIN = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Guessing Game</title>
</head>
<body>
<h1>I win! Your number is {guess}</h1>

</body>
</html>
"""


@app.route("/", methods=["GET", "POST"])
def guessing_game_3():
    if request.method == "GET":
        return START.format(0, 1000)
    else:
        min_number = int(request.form.get("min"))
        max_number = int(request.form.get("max"))
        player_answer = request.form.get("player_answer")
        guess = int(request.form.get("guess", 500))

        if player_answer == "too big":
            max_number = guess
        elif player_answer == "too small":
            min_number = guess
        elif player_answer == "you won":
            return WIN.format(guess=guess)

        guess = (max_number - min_number) // 2 + min_number

        return GUESSING.format(guess=guess, min=min_number, max=max_number)


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
