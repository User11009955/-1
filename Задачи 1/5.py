class BigBell:
    def __init__(self) -> None:
        self.count = 0
    
    def sound(self):
        self.count += 1
        if self.count % 2 == 1:
            print('ding')
        else:
            print('dong')