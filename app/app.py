from flask import Flask, render_template, request
import random

from functions import game_logic, test_advantage, attack, test_who_won

app = Flask(__name__)

first, second = game_logic()
test_advantage(first, second)


@app.route('/', methods=['POST', 'GET'])
def index():
    # Creating variables based on who's first and second
    if first.owner == "computer":
        computer = first
        player = second
    else:
        computer = second
        player = first

    if first.owner == "computer" and computer.battle_counter == 0:
        print(computer.name)
        computer.battle_counter = 1
        attack_name = random.choice(computer.type_attacks)
        attack(computer, player, attack_name)

    if request.method == 'POST':
        attack_name = request.form['attack_btn']
        attack(player, computer, attack_name)

        attack_name = random.choice(computer.type_attacks)
        attack(computer, player, attack_name)

    # TEST IF SOMEONE WON/LOOSE
    if first.life <= 0 or second.life <= 0:
        test_who_won(first, second)
    return render_template(
        'index.html', computer=computer, player=player
    )


# @app.route('/battle/', methods=["POST"])
# def battle_app():
#     if request.method == 'POST':
#         battle()
#     return render_template(
#         'index.html', computer=computer, player=player
#     )

if __name__ == "__main__":
    app.run(debug=True)
