# Компоненты автомобиля
from abc import ABC

class Engine:
    def __init__(self, engine_type):
        self.engine_type = engine_type

    def __str__(self):
        return f"Двигатель: {self.engine_type}"


class Transmission:
    def __init__(self, transmission_type):
        self.transmission_type = transmission_type

    def __str__(self):
        return f"Трансмиссия: {self.transmission_type}"


class Body:
    def __init__(self, body_type):
        self.body_type = body_type

    def __str__(self):
        return f"Кузов: {self.body_type}"


# Интерфейс строителя
class CarBuilder(ABC):
    def __init__(self):
        self.engine = None
        self.transmission = None
        self.body = None

    def set_engine(self, engine):
        self.engine = engine

    def set_transmission(self, transmission):
        self.transmission = transmission

    def set_body(self, body):
        self.body = body

    def get_car(self):
        return Car(self.engine, self.transmission, self.body)


# Конкретные строители
class SedanBuilder(CarBuilder):
    def __init__(self):
        self.set_engine(Engine("V6"))
        self.set_transmission(Transmission("Автоматическая"))
        self.set_body(Body("Седан"))


class SUVBuilder(CarBuilder):
    def __init__(self):
        self.set_engine(Engine("V8"))
        self.set_transmission(Transmission("Ручная"))
        self.set_body(Body("Внедорожник"))


# Директор
class CarDirector:
    def __init__(self, builder):
        self.builder = builder

    def construct_car(self):
        return self.builder.get_car()


# Продукт
class Car:
    def __init__(self, engine, transmission, body):
        self.engine = engine
        self.transmission = transmission
        self.body = body

    def __str__(self):
        return f"{self.body}\n{self.engine}\n{self.transmission}"


# Использование
sedan_builder = SedanBuilder()
director = CarDirector(sedan_builder)
sedan = director.construct_car()
print("Создан седан:", sedan, "\n")

suv_builder = SUVBuilder()
director = CarDirector(suv_builder)
suv = director.construct_car()
print("Создан внедорожник:", suv)
