from abc import ABC, abstractmethod


class FileSystemElement(ABC):
    @abstractmethod
    def display(self):
        pass

    @abstractmethod
    def get_size(self):
        pass

class File(FileSystemElement):
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def display(self):
        print(self.name)

    def get_size(self):
        return self.size

class Directory(FileSystemElement):
    def __init__(self, name):
        self.name = name
        self.elements = []

    def display(self):
        print(f"Directory: {self.name}")
        for element in self.elements:
            element.display()

    def get_size(self):
        total_size = 0
        for element in self.elements:
            total_size += element.get_size()
        return total_size

    def add(self, element):
        self.elements.append(element)

# Клиентский код
def main():
    root = Directory("root")
    home = Directory("home")
    user = Directory("user")

    file1 = File("file1.txt", 100)
    file2 = File("file2.txt", 200)
    file3 = File("file3.txt", 300)

    root.add(home)
    home.add(user)
    user.add(file1)
    user.add(file2)
    root.add(file3)

    root.display()
    print(f"\nTotal size: {root.get_size()} bytes")

if __name__ == "__main__":
    main()
