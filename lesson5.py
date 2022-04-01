from num2words import num2words

n = 0

while True:
    try:
        a, c, b = map(str, input('Введите выражение. Все через пробел.').split())
        if c == '/':
            while b != 0:
                try:
                    print('Ваш результат = ', num2words(eval(f'{a} {c} {b}'), lang='ru'))
                    break
                except (ZeroDivisionError):
                    n = n + 1
                    print('Делить на ноль нельзя, повтори ввод. ')
                    print('Ошибка номер {} '.format(n))
                    b = input('Введите второе число ')
            else:
                print('Ваш результат = ', num2words(eval(f'{a} {c} {b}'), lang='ru'))
    except (ValueError):
        print('Что-то пошло не так, повторите ввод! ')
    else:
        s = (input('Для выхода введите любым регистром: "Стоп". \nЧтобы продолжить, предлагаю нажать: "Enter" ').upper())
        if s == 'СТОП':
            break
        else:
            print('Погнали! ')
