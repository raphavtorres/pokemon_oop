# CARDS: https://www.youtube.com/watch?v=UYI959DTPBE&ab_channel=WebDevPills

# Pokemon mais rapido ataca primeiro
# velocidade igual == aleatorio
# 10% de chance de acertar crítico (dano dobrado)
# pokemon com vantagem ==> dobro de dano e perde meia vida apenas

def game_logic():
    bulbasaur = Grass("bulbasaur", 45, 8, 45)

class Pokemon():
    def __init__(self, name, life, attack, speed) -> None:
        self.name = name;
        self.life = life;
        self.attack = attack;
        self.speed = speed;
        self.advantage = False;

    def attack(self):
        if self.advantage:
            return self.attack * 2
        return self.attack

    def loose_life(self):
        if self.advantage:
            self.life -= self.life / 2
            return self.life
        self.life -= self.life
        return self.life


class Water(Pokemon):
    def __init__(self, name, life, attack, speed) -> None:
        super().__init__(name, life, attack, speed)


class Grass(Pokemon):
    def __init__(self, name, life, attack, speed) -> None:
        super().__init__(name, life, attack, speed)


class Fire(Pokemon):
    def __init__(self, name, life, attack, speed) -> None:
        super().__init__(name, life, attack, speed)
