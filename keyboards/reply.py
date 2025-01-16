from telebot.types import ReplyKeyboardMarkup, KeyboardButton

"""
Здесь собраны клавиатуры Reply
"""

def keyboard_muscles():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=3, one_time_keyboard=True)
    button_1 = KeyboardButton(text='Бицепс')
    button_2 = KeyboardButton(text='Трицепс')
    button_3 = KeyboardButton(text='Грудь')
    button_4 = KeyboardButton(text='Назад')
    button_5 = KeyboardButton(text='Ноги')
    button_6 = KeyboardButton(text='пресс')
    button_7 = KeyboardButton(text='Растяжка')
    button_8 = KeyboardButton(text='Разогревать')
    button_9 = KeyboardButton(text='лат')
    button_10 = KeyboardButton(text='Подколенное сухожилие')
    button_11 = KeyboardButton(text='Телята')
    button_12 = KeyboardButton(text='квадрицепс')
    button_13 = KeyboardButton(text='Трапеция')
    button_14 = KeyboardButton(text='Плечи')
    button_15 = KeyboardButton(text='Ягодицы')

    keyboard.add(button_1,button_2, button_3, button_4, button_5, button_6, button_7, button_8, button_9, button_10, button_11, button_12, button_13, button_14, button_15)
    return keyboard

def keyboard_sets():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2, one_time_keyboard=True)
    button1= KeyboardButton(text='Легкий')
    button2 = KeyboardButton(text='Средний')
    button3 = KeyboardButton(text='Тяжелый')
    button4 = KeyboardButton(text='Назад')

    keyboard.add(button1, button2, button3, button4)
    return keyboard

def keyboard_start():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2, one_time_keyboard=True)

    button_1= KeyboardButton(text='/Тренировки')
    button_2 = KeyboardButton(text='/help')
    button_3 = KeyboardButton(text='/history')
    button_4 = KeyboardButton(text='/cancel')

    keyboard.add(button_1, button_2, button_3, button_4)
    return keyboard
def keyboard_trenerovka_id():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2, one_time_keyboard=True)

    button_1 = KeyboardButton(text='ЕЩЕ')
    button_2 = KeyboardButton(text='НАЗАД')

    keyboard.add(button_1, button_2)
    return keyboard

def keyboard_trenerovka_id_2():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2, one_time_keyboard=True)

    button_1 = KeyboardButton(text='Далее')
    button_2 = KeyboardButton(text='НАЗАД')

    keyboard.add(button_1, button_2)
    return keyboard