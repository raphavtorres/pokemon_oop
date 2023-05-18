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
        dialog_attack = attack(computer, player, attack_name)
    else:
        dialog_attack = ["PLAYER FIRST! DO YOUR MOVE..."]

    if request.method == 'POST':
        # PLAYER ATTACK
        attack_name = request.form['attack_btn']
        dialog_attack = attack(player, computer, attack_name)

        # COMPUTER ATTACK
        attack_name = random.choice(computer.type_attacks)
        dialog_attack_pc = attack(computer, player, attack_name)
        for msg in dialog_attack_pc:
            dialog_attack.append(msg)

        # TEST IF SOMEONE WON/LOOSE
        if first.life <= 0 or second.life <= 0:
            dialog_test_won = test_who_won(first, second)
            for msg in dialog_test_won:
                dialog_attack.append(msg)

        return render_template(
            'index.html', computer=computer, player=player, dialog=dialog_attack
        )

    # dialog = ["Computer TURN", "WATER GUN ATTACK", "Computer DAMAGE = 8"]
    return render_template(
        'index.html', computer=computer, player=player, dialog=dialog_attack
    )


@app.route('/battle/', methods=["GET", "POST"])
def battle_app():
    if request.method == 'POST':
        return render_template(
            'index.html'
        )
    else:
        return render_template(
            'character.html'
        )

if __name__ == "__main__":
    app.run(debug=True)
