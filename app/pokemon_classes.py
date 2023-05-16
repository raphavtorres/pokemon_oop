# CARDS: https://www.youtube.com/watch?v=UYI959DTPBE&ab_channel=WebDevPills
# CHARACTERS INFO: https://pokemondb.net/pokedex/bulbasaur

import random


class Pokemon():
    def __init__(self, name, life, damage, speed) -> None:
        self._name = name
        self._life = life
        self._damage = damage
        self._speed = speed
        self._advantage = False

    @property
    def name(self):
        return self._name 
    
    @property
    def life(self):
        return self._life
    
    @property
    def damage(self):
        return self._damage
    
    @property
    def speed(self):
        return self._speed

    def attack(self):
        list_choice = [self._damage, self._damage * 1.5]
        # 10% de chance de acertar crítico (dano dobrado)
        attack = random.choices(list_choice, weights=(90, 10), k=1)
        if self._advantage:
            return attack * 2
        return attack

    
    # pokemon com vantagem ==> dobro de dano e perde meia vida apenas
    def loose_life(self, damage_received):
        if self._advantage:
            self._life -= damage_received / 2
            return self._life
        self._life -= damage_received
        return self._life


class Water(Pokemon):
    def __init__(self, name, life, damage, speed):
        super().__init__(name, life, damage, speed)
        self.type_attacks = ["Attack 1", "Ataque 2"]


class Grass(Pokemon):
    def __init__(self, name, life, damage, speed):
        super().__init__(name, life, damage, speed)
        self.type_attacks = ["Attack 1", "Ataque 2"]


class Fire(Pokemon):
    def __init__(self, name, life, damage, speed):
        super().__init__(name, life, damage, speed)
        self.type_attacks = ["Attack 1", "Ataque 2"]


def game_logic():
    # CREATING POKEMONS 
    bulbasaur = Grass("bulbasaur", 45, 9, 45)
    charmander = Fire("charmander", 39, 10, 65)
    squirtle = Water("squirtle", 44, 8, 43)

    pokemon_list = [bulbasaur, charmander, squirtle]
    computer = random.choice(pokemon_list).name

    person_choice = input("Pokemon name [0b/1c/2s] >> ")
    if person_choice == "0":
        player = bulbasaur
    elif person_choice == "1":
        player = charmander
    elif person_choice == "2":
        player = squirtle

    # Pokemon mais rapido ataca primeiro
    if computer.speed > player.speed:
        # computer starts first
        ...
    # Velocidade igual == aleatorio
    elif computer.speed == player.speed:
        # random start
        ...
    else:
        #player starts first
        ...


game_logic()
