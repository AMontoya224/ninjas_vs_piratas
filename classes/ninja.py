class Ninja:

    def __init__(self, name):
        self.name = name
        self.strength = 12
        self.speed = 10
        self.health = 100
    
    def show_stats( self ):
        print(f"{self.name.upper()}\nFuerza: {self.strength}\nFactor de curación: {self.speed}\nVida: {self.health}\n")
        return self.health

    def attack(self, enemigo):
        enemigo.health -= self.strength
        return self
    
    def criticAttack(self, enemigo):
        self.health -= (self.strength - self.speed) * 0.75
        enemigo.health -= self.strength * 1.5
        return self
    
    def cure(self):
        self.health += self.speed
        return self