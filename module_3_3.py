# Задача "Распаковка":


def print_params(a = 1, b = 'строка', c = True):                # функцию print_params(a = 1, b = 'строка', c = True),
                                                                # которая принимает три параметра со значениями по умолчанию
    print(f'a = {a}, b = {b}, c = {c}')
    return a, b, c


# Вывод результатов:
print_params()
print_params(2, 'новая строка', False)
print_params(c = False, b = 'новая булева переменная')


values_list = [3, 'новая строка 1', True]                       # Список values_list с тремя элементами разных типов
values_dict = {'a': 4, 'b': 'новая строка 2', 'c': False}       # словарь values_dict с тремя ключами, соответствующими
                                                                # параметрам функции
print_params(*values_list)                                      # Передайте values_list в функцию print_params,
                                                                # используя распаковку параметров (* для списка)
print_params(**values_dict)                                     # Передайте values_list в функцию print_params,
                                                                # используя распаковку параметров (** для словаря)


values_list_2 = [54.32, 'Строка']                               #  Cписок values_list_2 с двумя элементами разных типов
print_params(*values_list_2, 42)

# Обратите внимание, что если в списке есть необязательные параметры, распаковка не сработает