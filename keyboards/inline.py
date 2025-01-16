from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery, Message
from loader import bot


"""
Здесь собраны инлайн клавиатруры.
"""

def keyboard_step1():
    keyboard = InlineKeyboardMarkup(row_width=2)

    button_1 = InlineKeyboardButton(text='Имя', callback_data='user_name')
    button_2 = InlineKeyboardButton(text='Вес', callback_data='weight')
    button_3 = InlineKeyboardButton(text='Рост', callback_data='height')
    button_4 = InlineKeyboardButton(text='Возраст', callback_data='age')
    button_5 = InlineKeyboardButton(text='Пол', callback_data='gender')
    button_6 = InlineKeyboardButton(text='Далее', callback_data='further')

    keyboard.add(button_1, button_2, button_3, button_4, button_5, button_6
                 )
    return keyboard

def keyboard_start():
    keyboard = InlineKeyboardMarkup(row_width=2)

    button_1= InlineKeyboardButton(text='Тренировки', callback_data='trenerovka')
    button_2 = InlineKeyboardButton(text='Питание', callback_data='macronutrion_racion')
    button_3 = InlineKeyboardButton(text='Полезные советы', callback_data='advice')
    button_4 = InlineKeyboardButton(text='Составить программу', callback_data='make_programs')

    keyboard.add(button_1, button_2, button_3, button_4)
    return keyboard

def keyboard_step():
    keyboard = InlineKeyboardMarkup(row_width=2)

    button_1 = InlineKeyboardButton(text='Изменить свои данные', callback_data='change')
    button_2 = InlineKeyboardButton(text='История тренировок', callback_data='history_trenerovka')
    button_3 = InlineKeyboardButton(text='Предложенные ранее программы', callback_data='history_programs')
    button_4 = InlineKeyboardButton(text='Назад', callback_data='callback')
    button_5 = InlineKeyboardButton(text='Составить новую программу питания', callback_data='macronutrion_racion')
    button_6 = InlineKeyboardButton(text="Составить новую программу тренировок", callback_data='trenerovka')

    keyboard.add(button_1, button_2, button_3, button_4, button_5, button_6)
    return keyboard

def keyboard_step2():
    keyboard = InlineKeyboardMarkup(row_width=2)
    button_1 = InlineKeyboardButton(text='Продолжить', callback_data='continue')
    button_2 = InlineKeyboardButton(text='Изменить', callback_data='change')
    keyboard.row(button_1, button_2)

    return keyboard

def keyboard_save():
    keyboard = InlineKeyboardMarkup(row_width=2)
    button_1 = InlineKeyboardButton(text='Сохранить', callback_data='save')
    button_2 = InlineKeyboardButton(text='Изменить', callback_data='change')
    keyboard.row(button_1, button_2)

    return keyboard


def keyboard_muscles():
    keyboard = InlineKeyboardMarkup(row_width=5)
    button_1 = InlineKeyboardButton(text='Бицепсы', callback_data='Biceps')
    button_2 = InlineKeyboardButton(text='Трицепсы', url="https://work-out-api1.p.rapidapi.com/search")
    button_3 = InlineKeyboardButton(text='Грудь', url="https://work-out-api1.p.rapidapi.com/search")
    button_4 = InlineKeyboardButton(text='Назад', url="https://work-out-api1.p.rapidapi.com/search")
    button_5 = InlineKeyboardButton(text='Ноги', url="https://work-out-api1.p.rapidapi.com/search")
    button_6 = InlineKeyboardButton(text='Пресс', url="https://work-out-api1.p.rapidapi.com/search")
    button_7 = InlineKeyboardButton(text='Растяжка', url="https://work-out-api1.p.rapidapi.com/search")
    button_8 = InlineKeyboardButton(text='Разогревать', url="https://work-out-api1.p.rapidapi.com/search")
    button_9 = InlineKeyboardButton(text='лат', url="https://work-out-api1.p.rapidapi.com/search")
    button_10 = InlineKeyboardButton(text='Подколенное сухожилие', url="https://work-out-api1.p.rapidapi.com/search")
    button_11 = InlineKeyboardButton(text='Телята', url="https://work-out-api1.p.rapidapi.com/search")
    button_12 = InlineKeyboardButton(text='квадрицепсы', url="https://work-out-api1.p.rapidapi.com/search")
    button_13 = InlineKeyboardButton(text='Трапеция', url="https://work-out-api1.p.rapidapi.com/search")
    button_14 = InlineKeyboardButton(text='Плечи', url="https://work-out-api1.p.rapidapi.com/search")
    button_15 = InlineKeyboardButton(text='Ягодицы', url="https://work-out-api1.p.rapidapi.com/search")

    keyboard.add(button_1, button_2, button_3, button_4, button_5, button_6, button_7,
                 button_8, button_9, button_10, button_11, button_12, button_13, button_14, button_15)
    return keyboard

# @bot.callback_query_handler(func=lambda callback_data: True)
# def callback_query(call: CallbackQuery):
#     if call.message:
#         if call.data == 'trenerovka':
#             bot.answer_callback_query(call.id, text='Выбераем тренеровку')
#         elif call.data == 'macronutrion_racion':
#             bot.answer_callback_query(call.id, text='Выбераем питание')
#         elif call.data == 'advice':
#             bot.answer_callback_query(call.id, text='Выбераем что-то')
#         elif call.data == 'make_programs':
#             bot.answer_callback_query(call.id, text='Составим программу')


# @bot.message_handler(func= lambda message: True)
# def message_inline_button(message: Message):
#     bot.send_message(message.chat.id, "Выберите, чем будем заниматься?", reply_markup=keyboard_start())
