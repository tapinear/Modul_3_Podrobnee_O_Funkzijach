# Задача "Однокоренные":


def single_root_words(root_word, *other_words):                 # Функция single_root_words с параметрами в ней
                                                                # root_word и *other_words
    same_words = []                                             # Пустой список same_words внутри функйии single_root_words,
                                                                # который пополнится нужными словами
    for word in other_words:                                    # Цикл for для перебора подходящих слов
        if root_word.lower() in word.lower() or word.lower() in root_word.lower():  # Условие согласно которого подходящее
                                                                                    # слово добавляется в список same_words
            same_words.append(word)
    return same_words


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)
