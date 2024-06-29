# Задача "Счётчик вызовов":

calls = 0


#  Функция считает количество вызовов
def count_calls():
    global calls
    calls += 1
    return calls


# Функция выводит длину, верхний и нижний регистры введенной строки, а также считает количество вызовов
def string_info(string):
    count_calls()
    return len(string), string.upper(), string.lower()


# Функция проверяет, содержит ли введенная строка любую из переданных в списке
def is_contains(string, list_to_search):
    count_calls()
    return string.upper() in [item.upper() for item in list_to_search]


# Testing
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic']))    # No matches
print(calls)
