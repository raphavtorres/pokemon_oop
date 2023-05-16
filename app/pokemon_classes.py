# CARDS: https://www.youtube.com/watch?v=UYI959DTPBE&ab_channel=WebDevPills
# CHARACTERS INFO: https://pokemondb.net/pokedex/bulbasaur

# Pokemon mais rapido ataca primeiro
# velocidade igual == aleatorio
# 10% de chance de acertar crítico (dano dobrado)
# pokemon com vantagem ==> dobro de dano e perde meia vida apenas
import random

def game_logic():
    bulbasaur = Grass("bulbasaur", 45, 9, 45)
    charmander = Fire("charmander", 39, 10, 65)
    squirtle = Water("squirtle", 44, 8, 43)

class Pokemon():
    def __init__(self, name, life, damage, speed) -> None:
        self.name = name;
        self.life = life;
        self.damage = damage;
        self.speed = speed;
        self.advantage = False;

    def attack(self):
        list_choice = [self.damage, self.damage * 1.5]
        attack = random.choices(list_choice, weights=(90, 10), k=1)
        if self.advantage:
            return attack * 2
        return attack

    def loose_life(self, damage_received):
        if self.advantage:
            self.life -= damage_received / 2
            return self.life
        self.life -= damage_received
        return self.life

    @property
    def name(self):
        return self.name
    
    @property
    def life(self):
        return self.life
    
    @property
    def damage(self):
        return self.damage
    
    @property
    def speed(self):
        return self.speed
    
    @property
    def speed(self):
        return self.speed

class Water(Pokemon):
    def __init__(self, name, life, damage, speed) -> None:
        super().__init__(name, life, damage, speed)


class Grass(Pokemon):
    def __init__(self, name, life, damage, speed) -> None:
        super().__init__(name, life, damage, speed)


class Fire(Pokemon):
    def __init__(self, name, life, damage, speed) -> None:
        super().__init__(name, life, damage, speed)
