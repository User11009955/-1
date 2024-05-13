from abc import ABC, abstractmethod

# Абстрактная фабрика
class CarFactory(ABC):
    @abstractmethod
    def produce_car(self):
        pass

# Конкретные фабрики
class ElectricCarFactory(CarFactory):
    def produce_car(self):
        return ElectricCar()

class PetrolCarFactory(CarFactory):
    def produce_car(self):
        return PetrolCar()

class HybridCarFactory(CarFactory):
    def produce_car(self):
        return HybridCar()

# Абстрактный класс Car
class Car(ABC):
    @abstractmethod
    def drive(self):
        pass

# Конкретные классы автомобилей
class ElectricCar(Car):
    def drive(self):
        print("Driving an electric car.")

class PetrolCar(Car):
    def drive(self):
        print("Driving a petrol car.")

class HybridCar(Car):
    def drive(self):
        print("Driving a hybrid car.")

# Использование фабрик для создания автомобилей
electric_factory = ElectricCarFactory()
petrol_factory = PetrolCarFactory()
hybrid_factory = HybridCarFactory()

electric_car = electric_factory.produce_car()
petrol_car = petrol_factory.produce_car()
hybrid_car = hybrid_factory.produce_car()

electric_car.drive()
petrol_car.drive()
hybrid_car.drive()
