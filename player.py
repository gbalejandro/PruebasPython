class Player(object):
    vocation = "No vocation"
    spell = "Puff"
    movement_speed = "50"

    def __init__(self,**kwargs):
        self.hit_points = kwargs.get("hit_points",50)
        self.mana = kwargs.get("mana",50)

    def __str__(self):
        return "cadena {} "format("algo")

    def cast_spell(self):
        return self.spell

class Sorcerer(Player):
    vocation = "Sorcerer"
    spell = "Utevo Lux"
    movement_speed = "20"

class Knight(Player):
    vocation = "Knight"
    spell = "Exori"
    movement_speed = "60"