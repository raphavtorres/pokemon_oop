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
    while True:
        attack_name = "COMPUTER"
        if first.owner == "player":
            attack_name = input("Choose attack >> ")

        # FIRST ATTACK
        attack_amount = first.attack(attack_name)
        second.loose_life(attack_amount)
        test_type_attack(attack_amount)
        print("ATTACK", first.owner, attack_amount)
        print("LIFE ", first.owner, first.life)
        print()

        if second.owner == "player":
            attack_name = input("Choose attack >> ")
        # SECOND ATTACK
        attack_amount = second.attack(attack_name)
        first.loose_life(attack_amount)
        test_type_attack(attack_amount)
        print("ATTACK", second.owner, attack_amount)
        print("LIFE", second.owner, second.life)
        print()

        if first.life <= 0 or second.life <= 0:
            break
        
    
    test_who_won(first, second)
        # Let player choose an attack
        # Test who dies

def test_who_won(first, second):
    print(first.life)
    print(second.life)
    if first.life < second.life:
        print(second.owner, "WON!")
    else:
        print(first.owner, "WON!")
    print("GAME OVER")


def game_logic():
    # first = Grass("bulbasaur", 45, 9, 45)
    # CREATING POKEMONS
    bulbasaur, charmander, squirtle = create_pokemon()

    # Computer choice
    pokemon_list = [bulbasaur, charmander, squirtle]
    computer = random.choice(pokemon_list)
    print(computer)
    computer.owner = "computer"

    # Person choice
    player_choice = input("Pokemon name [0b/1c/2s] >> ")
    if player_choice == "0":
        player = bulbasaur
    elif player_choice == "1":
        player = charmander
    elif player_choice == "2":
        player = squirtle
    player.owner = "player"

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
