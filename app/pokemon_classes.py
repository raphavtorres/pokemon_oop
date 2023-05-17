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

    @property
    def advantage(self):
        return self._advantage

    @advantage.setter
    def advantage(self, advantage):
        self._advantage = advantage

    def attack(self):
        list_choice = [self._damage, self._damage * 1.5, 0]
        # 10% de chance de acertar crítico (dano dobrado)
        attack = random.choices(list_choice, weights=(0.8, 0.1, 0.1), k=1)[0]
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
        self._category = "water"
        self._type_attacks = ["Attack 1", "Ataque 2"]

    @property
    def category(self):
        return self._category


class Grass(Pokemon):
    def __init__(self, name, life, damage, speed):
        super().__init__(name, life, damage, speed)
        self._category = "grass"
        self._type_attacks = ["Attack 1", "Ataque 2"]

    @property
    def category(self):
        return self._category


class Fire(Pokemon):
    def __init__(self, name, life, damage, speed):
        super().__init__(name, life, damage, speed)
        self._category = "fire"
        self._type_attacks = ["Attack 1", "Ataque 2"]

    @property
    def category(self):
        return self._category
