class GameSettings:
    __instance = None

    def __init__(self):
        self.volume = 50
        self.difficulty = "Normal"

    @staticmethod
    def get_instance():
        if GameSettings.__instance is None:
            GameSettings.__instance = GameSettings()
        return GameSettings.__instance

# Пример использования
settings1 = GameSettings.get_instance()
settings2 = GameSettings.get_instance()

# Проверим, что это один и тот же объект
print(settings1 is settings2)  # Выведет True

# Меняем настройки в одном объекте
settings1.volume = 70
settings1.difficulty = "Hard"

# Проверяем, что настройки изменились в обоих объектах
print(settings2.volume)  # Выведет 70
print(settings2.difficulty)  # Выведет "Hard"
