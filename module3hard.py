# Задание "Раз, два, три, четыре, пять ... Это не всё?":


data_structure = [[1, 2, 3], {'a': 4, 'b': 5}, (6, {'cube': 7, 'drum': 8}),
                  "Hello", ((), [{(2, 'Urban', ('Urban2', 35))}])]


def count_numbers_and_strings(data_structure):  # Функция чисел и строк
    total_sum = 0                               # Счётчит чисел
    total_length = 0                            # Счётчит длин строк

    def recursive_count(structure):                             # Функция вычисления суммы чисел и длин строк
        nonlocal total_sum, total_length                        # Вызов глобальных переменных
        if isinstance(structure, int):                          # Функция проверяет является ли переменная числом
            total_sum += structure
        elif isinstance(structure, str):                        # Функция проверяет является ли переменная строкой
            total_length += len(structure)
        elif isinstance(structure, (list, tuple, set)):         # Функция проверяет является ли переменная списком, кортежем,множеством
            for item in structure:
                recursive_count(item)
        elif isinstance(structure, dict):                       # Функция проверяет является ли переменная словарем
            for keys, values in structure.items():
                recursive_count(keys)
                recursive_count(values)

    recursive_count(data_structure)
    return f'Общая сумма всех чисел и сток: {total_sum + total_length}'


# Проверка решения
print(count_numbers_and_strings(data_structure))
