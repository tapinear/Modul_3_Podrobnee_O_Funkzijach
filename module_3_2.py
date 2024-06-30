# Задача "Рассылка писем":

# Функция отправки письма, с провекой условий
def send_email(message, recipient, sender="university.help@gmail.com"):
    if ('@' not in recipient or '@' not in sender or not recipient.endswith(('.com', '.ru', '.net'))
            or not sender.endswith(('.com', '.ru', '.net'))):   # Проверка условий когда переменные recipient и sender
        # не содержат символ @ и не содержат не содержат в конце строки окончания .com', '.ru', '.net
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
    elif recipient == sender:   # Проверка условия чтобы отправитель и получатель не были одними и теми же
        print("Нельзя отправить письмо самому себе!")
    elif sender == "university.help@gmail.com":     # Условие проверки удачной отправки письма
        print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}')
    else:   # Условие при котором письмо отправляется не почтового ящика администратора
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса  {sender} на адрес {recipient}.')


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru',
           sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
