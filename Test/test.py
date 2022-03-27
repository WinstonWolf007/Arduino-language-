class Player:
    def __init__(self, health, attack, velocity):
        self.health = health
        self.attack = attack
        self.velocity = velocity

    def display(self):
        print(self.health, self.attack, self.velocity)


player1 = Player(12, 4, 3)
player2 = Player(20, 10, 2)

player1.display()
player2.display()
