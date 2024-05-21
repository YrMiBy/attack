import random

class Hero:
    def __init__(self, name, health=100, attack_power=20): # Имя, здоровье, сила удара
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, other): # функция уменьшения здоровья (повреждение) героя после нанесения удара
        damage = random.randint(1, self.attack_power) # сила удара от 1 20
        other.health -= damage # уменшение здоровья другого бойца
        print(f"{self.name} нанес {damage} урона {other.name}") # один боуц нанес силой удара урон другому бойцу

    def is_alive(self):
        if self.health > 0:
            return True
        else:
            return False

class Game:
    def __init__(self, player, computer):
        self.player = player
        self.computer = computer

    def start(self):
        current_player = self.computer # текущий игрок
        while self.player.is_alive() and self.computer.is_alive(): # цикл боя, пока здоровье  игроков > 0 (True)
            if current_player == self.player:
                current_player.attack(self.computer)
            else:
                current_player.attack(self.player)
            if current_player == self.computer:
                current_player = self.player
            else:
                current_player = self.computer

        if self.player.is_alive(): # True
            winner = self.player # Победитель
        else:
            winner = self.computer
        print(f"{winner.name} победил!")

# Создание бойцов
player = Hero("Игрок")
computer = Hero("Компьютер")

# Создание игры и начало игры
game = Game(player, computer)
game.start()