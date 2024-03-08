class User:
    def __init__(self, name):
        self.name = name

    def send_message(self, user, message):
        print(f"User {self.name} sent a message to {user.name}: {message}")

    def post(self, message):
        print(f"User {self.name} posted on their wall: {message}")

    def info(self):
        return ""

    def describe(self):
        print(f"User: {self.name}")
        print(self.info())


class Person(User):
    def __init__(self, name, birth_date):
        super().__init__(name)
        self.birth_date = birth_date

    def info(self):
        return f"Дата рождения: {self.birth_date}"

    def subscribe(self, user):
        print(f"User {self.name} subscribed to {user.name}")


class Community(User):
    def __init__(self, name, description):
        super().__init__(name)
        self.description = description

    def info(self):
        return f"Описание: {self.description}"
