from flask import Flask, render_template, request

from functions import game_logic, battle

app = Flask(__name__)

first, second = game_logic()


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        attack_name = request.form['attack_btn']
        battle(first, second, attack_name)

    if first.owner == "computer":
        computer = first
        player = second
    else:
        computer = second
        player = first

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
