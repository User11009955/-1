from abc import ABC, abstractmethod

# Интерфейс для источника данных
class DataSource(ABC):
    @abstractmethod
    def read_data(self):
        pass

# Класс, читающий данные из текстового файла
class FileDataSource(DataSource):
    def __init__(self, file_path):
        self.file_path = file_path

    def read_data(self):
        with open(self.file_path, 'r') as file:
            return file.read()

# Класс, имитирующий чтение данных из базы данных
class DatabaseDataSource:
    def __init__(self, connection_string):
        self.connection_string = connection_string

    def fetch_data(self):
        # Чтение данных из базы данных (имитация)
        return "Data fetched from database using connection string: " + self.connection_string

# Адаптер для работы с базой данных через интерфейс DataSource
class DatabaseAdapter(DataSource):
    def __init__(self, database_source):
        self.database_source = database_source

    def read_data(self):
        return self.database_source.fetch_data()

# Пример использования
file_source = FileDataSource("data.txt")
print(file_source.read_data())

database_source = DatabaseDataSource("database_connection_string")
database_adapter = DatabaseAdapter(database_source)
print(database_adapter.read_data())
