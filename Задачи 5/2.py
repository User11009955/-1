def check_password(func):
    if input('Введите пароль: ') == '':
        return func
    else:
        raise Exception('Неверный пароль')
    
@check_password  
def fibbonachi(n):
    a, b = 0, 1
    for i in range(n):
        a, b = a + b, a
    return a

print(fibbonachi(3))