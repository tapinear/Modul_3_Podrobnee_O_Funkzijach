# Задача "Рекурсивное умножение цифр":


def get_multiplied_digits(number):                                      # Функция get_multiplied_digits и параметр number в ней
    str_number = str(number)                                            # Переменная str_number и строковое представление(str) числа number в неё
    first = int(str_number[0])                                          # Переменная first и запиcь в неё первого символа из str_number в числовом представлении(int)
    if len(str_number) > 1:                                             # Условие когда длина str_number больше 1, иначе не получиться взять срез str_number[1:]
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        return first


# Testing
result = get_multiplied_digits(40203)
print(result)
