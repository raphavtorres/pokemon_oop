import random

from pokemon_classes import Fire, Grass, Water


def create_pokemon():
    """Creates the objects of pokemon"""
    bulbasaur = Grass("bulbasaur", 45, 9, 45)
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
    if attack_amount == attacker.damage * 2:
        print("CRITICAL")
    elif attack_amount == attacker.damage * 1.5:
        print("ADVANTAGE MOVE")
    elif attack_amount == 0:
        print("MISSED")


def attack(attacker, attacked, attack_name):
    print("OWNER:", attacker.owner)

    # FIRST ATTACK
    attack_amount = attacker.attack(attack_name)
    attacked.loose_life(attack_amount)
    test_type_attack(attack_amount, attacker)
    print(attacker.owner, "DAMAGE =", attack_amount)
    print()


def test_who_won(first, second):
    print(first.life)
    print(second.life)
    if first.life < second.life:
        print(second.owner, "WON!")
    else:
        print(first.owner, "WON!")
    print("GAME OVER")


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
