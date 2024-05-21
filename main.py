from abc import ABC, abstractmethod

class Weapon(ABC): # абстрактный класс оружие
    @abstractmethod
    def attack(self): # абстрактная функция атака
        pass

class Sword(Weapon): # класс меч
    def attack(self): # функция удар мячем
        return "удар мечом"

    def v_attack(self): # функция выбор меча
        return 'выбрал меч'

class Bow(Weapon): # класс лук
    def attack(self): # функция стрельба из лука
        return "стрельба из лука"

    def v_attack(self): # функция выбор лука
        return 'выбрал лук'

class Fighter: # класс боец
    def __init__(self, name):
        self.name = name
        self.weapon = None

    def changeWeapon(self, weapon): # функция смены оружия
        self.weapon = weapon

    def attack(self, monster):
        if self.weapon:
            print(f'{self.name}  {self.weapon.v_attack()}.')
            print(f"{self.name} наносит {self.weapon.attack()}.")
            print(f"Монстр побежден!")
        else:
            print(f"{self.name} не выбрал оружие. Не может атаковать.")


class Monster: # класс Monster
    def __init__(self, name, sila):
        self.name = name
        self.sila = sila

    def monster_sila(self):
        if self.sila <= 0:
            print('Монстр уничтожен')
        else:
            self.sila = self.sila - 2 # Уменьшение силы монстра при нанесении удара
            print(f'cила монстра равна {self.sila}')

# объекты бойца и монстра
fighter = Fighter("Боец")
monster = Monster("Монстр", 10)

# Демонстрация боя
sword = Sword() # объект меч
bow = Bow() # объект лук

fighter.changeWeapon(sword) # функция changeWeapon объекта fighter, в которую передается аргумент sword
fighter.attack(monster)
monster.monster_sila()

fighter.changeWeapon(bow)
fighter.attack(monster)
monster.monster_sila()