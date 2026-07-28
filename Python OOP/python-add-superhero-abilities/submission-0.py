class SuperHero:
    def __init__(self, name, power, health):
        self.name = name
        self.power = power
        self.health = health

    def attack(self):
        print(f"{self.name} attacks with {self.power}!")

    def heal(self):
        self.health += 10
        print(f"{self.name} heals 10 points. New health: {self.health}.")


catwoman = SuperHero("Catwoman", "Agility", 120)

catwoman.attack()
catwoman.heal()