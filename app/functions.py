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


def test_type_attack(attack_amount):
    if attack_amount > 15:
        print("CRITICAL")
    elif attack_amount == 0:
        print("MISSED")


def battle(first, second):
    # first = Grass("bulbasaur", 45, 9, 45)
    # second = Water("bulbasaur", 45, 9, 45)
    test_advantage(first, second)
    # while True:
    for i in range(5):
        attack_amount = first.attack()
        second.loose_life(attack_amount)
        test_type_attack(attack_amount)
        print("ATTACK F:", attack_amount)
        print("LIFE F:", first.life)

        attack_amount = second.attack()
        first.loose_life(attack_amount)
        test_type_attack(attack_amount)
        print("ATTACK S:", attack_amount)
        print("LIFE S:", first.life)
        print()

        # Let player choose an attack
        # Test who dies


def game_logic():
    # CREATING POKEMONS
    bulbasaur, charmander, squirtle = create_pokemon()

    pokemon_list = [bulbasaur, charmander, squirtle]
    computer = random.choice(pokemon_list)

    person_choice = input("Pokemon name [0b/1c/2s] >> ")
    if person_choice == "0":
        player = bulbasaur
    elif person_choice == "1":
        player = charmander
    elif person_choice == "2":
        player = squirtle
    first, second = start_first(computer, player)
    battle(first, second)


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
