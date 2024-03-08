def check_password(password):
    def decorator(func):
        if input('Введите пароль: ') == password:
            return func
        else:
            raise Exception('Неверный пароль')
    return decorator

@check_password('password')
def make_burger(typeOfMeat, withOnion=False, withTomato=True):
    # ...
    pass

# Проверка
make_burger('beef', withOnion=True)
