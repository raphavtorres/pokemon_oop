import random

from pokemon_classes import Fire, Grass, Water


def create_pokemon():
    """Creates the objects of pokemon"""
    bulbasaur = Grass("bulbasaur", 42, 9, 45)
    charmander = Fire("charmander", 39, 10, 65)
    squirtle = Water("squirtle", 44, 8, 43)
    return bulbasaur, charmander, squirtle


def start_first(computer, player):
    """Controls what pokemon will be the first to start the battle"""
    # Pokemon mais rapido ataca primeiro
    if computer.speed > player.speed:
        # computer starts first
        return computer, player

    # Velocidade igual == aleatorio
    elif computer.speed == player.speed:
        # random start
        random_start = [computer, player]
        first = random.choice(random_start)
        random_start.remove(first)
        second = random_start[0]
        return first, second

    # player starts first
    return player, computer


def test_type_attack(attack_amount, attacker):
    attack_type = ""
    if attack_amount == attacker.damage * 2:
        attack_type = f"{attacker.owner} HIT CRITICAL ATTACK"
    elif attack_amount == attacker.damage * 1.5:
       attack_type = f"{attacker.owner} HAS ADVANTAGE MOVE"
    elif attack_amount == 0:
        attack_type = f"{attacker.owner} MISSED 😿"
    return attack_type


def test_life_amount(attacker, attacked, dialog_attack):
    msg = ""
    if attacker.life <= 0 or attacked.life <= 0:
        dialog_test_won = test_who_won(attacker, attacked)
        for msg in dialog_test_won:
            dialog_attack.append(msg)
    elif attacker.owner == "computer":
        dialog_attack.append("YOUR TURN...")
    return dialog_attack


def attack(attacker, attacked, attack_name):
    dialog_attack = []
    dialog_attack.append(f"{attacker.owner.upper()} ATTACKING!")

    attack_amount = attacker.attack(attack_name)
    attacked.loose_life(attack_amount)
    attack_type = test_type_attack(attack_amount, attacker)
    dialog_attack.append(attack_type)
    dialog_attack.append(f"{attacker.owner.upper()} GAVE {attack_amount} OF DAMAGE!")

    dialog_attack = test_life_amount(attacker, attacked, dialog_attack)

    return dialog_attack


def test_who_won(first, second):
    dialog = []
    dialog.append(f"{first.owner} = {first.life}")
    dialog.append(f"{second.owner} = {second.life}")
    if first.life < second.life:
        dialog.append(f"{second.owner} WON!")
    else:
        dialog.append(f"{first.owner} WON!")
    dialog.append("GAME OVER!")
    return dialog


def game_logic():
    # Computer choice
    bulbasaur_comp, charmander_comp, squirtle_comp = create_pokemon()
    pokemon_list_computer = [bulbasaur_comp, charmander_comp, squirtle_comp]
    computer = random.choice(pokemon_list_computer)
    computer.owner = "computer"

    # Person choice
    bulbasaur_player, charmander_player, squirtle_player = create_pokemon()
    # pokemon_list_player = [bulbasaur_player, charmander_player, squirtle_player]
    player = squirtle_player
    player.owner = "player"

    first, second = start_first(computer, player)
    return first, second


def test_advantage(first, second):
    """Tests what pokemon has advantage based on the class
       and changes the category state in the object"""
    second.advantage = True
    if first.category == 'water' and second.category == 'grass':
        pass
    elif first.category == 'grass' and second.category == 'fire':
        pass
    elif first.category == 'fire' and second.category == 'water':
        pass
    elif first.category == second.category:
        second.advantage = False
    else:
        first.advantage = True
        second.advantage = False


game_logic()
