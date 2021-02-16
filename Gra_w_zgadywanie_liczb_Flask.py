from flask import Flask, request

app = Flask(__name__)

html_startowa = """
<!DOCTYPE html>
<html lang="pl">
<head>
    <meta charset="UTF-8">
    <title>Zgadnij liczbę</title>
</head>
<body>
<h1>Pomyśl liczbę od 0 do 1000, a komputer zgadnie ją w max 10 próbach!</h1>
<form action="" method="POST">
    <input type="hidden" name="min" value="{}"></input>
    <input type="hidden" name="max" value="{}"></input>
    <input type="submit" value="Przejdź dalej">
</form>
</body>
</html>
"""

html_glowna = """
<!DOCTYPE html>
<html lang="pl">
<head>
    <meta charset="UTF-8">
    <title>Zgadnij liczbę</title>
</head>
<body>
<h1>Wydaje mi się, że twoja liczba to: {guess}</h1>
<form action="" method="POST">
    <input type="submit" name="user_answer" value="Too big">
    <input type="submit" name="user_answer" value="Too small">
    <input type="submit" name="user_answer" value="You win">
    <input type="hidden" name="min" value="{min}">
    <input type="hidden" name="max" value="{max}">
    <input type="hidden" name="guess" value="{guess}">
</form>
</body>
</html>
"""

html_wygrana = """
<!DOCTYPE html>
<html lang="pl">
<head>
    <meta charset="UTF-8">
    <title>Zgadnij liczbę</title>
</head>
<body>
<h1>Hurra! Zgadłem. Twoja liczba to {guess}!!!</h1>

</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def user_answers():
    """Funkcja zwraca tekst wpisany przez użytkownika.
        :rtype: str
        :return: wartość wpisaną przez użytkownika ['too small', 'too big', 'you win']
        """
    if request.method == 'GET':
        return html_startowa.format(0, 1000)
    else:
        min_number = int(request.form.get("min"))
        max_number = int(request.form.get("max"))
        user_answer = request.form.get("user_answer")
        guess = int(request.form.get("guess", 500))
        if user_answer == "Too big":
            max_number = guess
        elif user_answer == "Too small":
            min_number = guess
        elif user_answer == "You win":
            return html_wygrana.format(guess=guess)
        guess = int((max_number - min_number) // 2) + min_number
        return html_glowna.format(guess=guess, min=min_number, max=max_number)

if __name__ == '__main__':
    app.run()
