from math import sqrt

class Weapon:
    def __init__(self, name, damage, range):
        self.name = name
        self.damage = damage
        self.range = range
    
    def hit(self, actor, target):
        if target.is_alive():
            if sqrt(abs(target.x - actor.x)**2 + abs(target.y - actor.y)**2) <= self.range:
                target.health -= self.damage
                print(f'Врагу нанесен урон оружием {self.name} в размере {self.damage}')
            else:
                print(f'Враг слишком далеко для оружия {self.name}')
        else:
            print('Враг уже повержен') 
    
    def __str__(self):
        return self.name

class BaseCharacter:
    def __init__(self, x, y, health):
        self.x = x
        self.y = y
        self.health = health

    def is_alive(self):
        return self.health > 0

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def get_damage(self,amount):
        print(self.health)
        self.health -= amount

    def get_coords(self):
        return self.x, self.y

class BaseEnemy(BaseCharacter):
    def __init__(self, x, y, weapon, health):
        super().__init__(x, y, health)
        self.weapon = weapon

    def hit(self, target):
        if isinstance(target, MainHero):
            target_weapons = target.weapons[target.current_weapon]
            target_weapons.hit(self, target)
        else:
            print("Могу ударить только Главного героя")

    def __str__(self):
        return f"Враг на позиции {self.get_coords()} с оружием {self.weapon}"
    
class MainHero(BaseCharacter):
    def __init__(self, x, y, name, health):
        super().__init__(x, y, health)
        self.name = name
        self.weapons = []
        self.current_weapon = 0

    def next_weapon(self):
        if self.weapons:
            if len(self.weapons) == 1:
                print('У меня только одно оружие')
            else:
                self.current_weapon = (self.current_weapon + 1) % len(self.weapons)
                print(f'Сменил оружие на {self.weapons[self.current_weapon].name}   {self.current_weapon}')
        else:
            print('Я безоружен')

    def add_weapon(self, weapon):
        if isinstance(weapon, Weapon):
            self.weapons.append(weapon)
            print(f'Подобрал {weapon.name}')
        else:
            print('Это не оружие')

    def hit(self, target):
        if self.weapons:
            if isinstance(target, BaseEnemy):
                target.hit(self)
            else:
                print("Могу ударить только Врага")
        else:
            print('Я безоружен')
    
    def heal(self, amount):
        self.health += amount if self.health + amount < 200 else 200 - self.health
        print(f'Полечился, теперь здоровья {self.health}')
        
    def __str__(self):
        return f"Главный герой {self.name} на позиции {self.get_coords()}"
# Ваш код

weapon1 = Weapon("Короткий меч", 5, 1)
weapon2 = Weapon("Длинный меч", 7, 2)
weapon3 = Weapon("Лук", 3, 10)
weapon4 = Weapon("Лазерная орбитальная пушка", 1000, 1000)
princess = BaseCharacter(100, 100, 100)
archer = BaseEnemy(50, 50, weapon3, 100)
armored_swordsman = BaseEnemy(10, 10, weapon2, 500)
archer.hit(armored_swordsman)
armored_swordsman.move(10, 10)
print(armored_swordsman.get_coords())
main_hero = MainHero(0, 0, "Король Артур", 200)
main_hero.hit(armored_swordsman)
main_hero.next_weapon()
main_hero.add_weapon(weapon1)
main_hero.hit(armored_swordsman)
main_hero.add_weapon(weapon4)
main_hero.hit(armored_swordsman)
main_hero.next_weapon()
main_hero.hit(princess)
main_hero.hit(armored_swordsman)
main_hero.hit(armored_swordsman)