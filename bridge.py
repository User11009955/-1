from abc import ABC, abstractmethod

class Device(ABC):
    @abstractmethod
    def turn_on(self):
        pass
    
    @abstractmethod
    def turn_off(self):
        pass
    
    @abstractmethod
    def set_state(self, state):
        pass

class TV(Device):
    def turn_on(self):
        print("TV включен")
    
    def turn_off(self):
        print("TV выключен")
    
    def set_state(self, state):
        print(f"Канал изменен на {state}")

class Light(Device):
    def turn_on(self):
        print("Лампочка включена")
    
    def turn_off(self):
        print("Лампочка выключена")
    
    def set_state(self, state):
        print(f"Яркость установлена на {state}")

class RemoteControl:
    def __init__(self, device):
        self.device = device

    def turn_on(self):
        self.device.turn_on()

    def turn_off(self):
        self.device.turn_off()

    def set_state(self, state):
        self.device.set_state(state)

class SonyTV(TV):
    pass

class SamsungTV(TV):
    pass

class PhilipsLight(Light):
    pass

class IKEALight(Light):
    pass

# Клиентский код
def main():
    sony_tv = SonyTV()
    samsung_tv = SamsungTV()
    philips_light = PhilipsLight()
    ikea_light = IKEALight()

    remote_for_sony = RemoteControl(sony_tv)
    remote_for_samsung = RemoteControl(samsung_tv)
    remote_for_philips = RemoteControl(philips_light)
    remote_for_ikea = RemoteControl(ikea_light)

    remote_for_sony.turn_on()
    remote_for_sony.set_state("HBO")
    remote_for_sony.turn_off()

    remote_for_samsung.turn_on()
    remote_for_samsung.set_state("CNN")
    remote_for_samsung.turn_off()

    remote_for_philips.turn_on()
    remote_for_philips.set_state("75%")
    remote_for_philips.turn_off()

    remote_for_ikea.turn_on()
    remote_for_ikea.set_state("50%")
    remote_for_ikea.turn_off()

if __name__ == "__main__":
    main()
