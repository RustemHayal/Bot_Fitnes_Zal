from loader import bot
from telebot.types import Message
from keyboards.reply import keyboard_muscles, keyboard_sets, keyboard_trenerovka_id, keyboard_trenerovka_id_2
from states.user_states import TrenerState
from database.command import history_save_user, muscle_record_check, save_trenerovka_dir, trenerovka
from handlers.custom_handlers.related import step
from keyboards.reply import keyboard_start
from googletrans import Translator


@bot.message_handler(state='*', commands=["trenerovka", "Тренировки"])
def handler_trenerovka(message: Message):
    """
    Обработчик команды Тренировки. Выбор группы мышц для тренировки.
    :param message:
    :return:
    """
    user_id = message.from_user.id
    if history_save_user(user_id, message):
        step(message)

    bot.send_message(chat_id=message.chat.id, text=f"Выберите группу мышц для тренеровок", reply_markup=keyboard_muscles())
    bot.set_state(message.from_user.id, TrenerState.muscul, message.chat.id)
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data_tren:
        data_tren["trenerovka"] = {"trenerovka": user_id}


@bot.message_handler(state=TrenerState.muscul)
def trenerovka_dir(message: Message):
    translator = Translator()
    muscle_en = translator.translate(message.text, 'en', 'ru').text
    muscle_ru = message.text
    print(muscle_ru, muscle_en)
    fetch_rows(message, muscle_en, muscle_ru, 0)

    bot.set_state(message.from_user.id, TrenerState.trenerovka_id, message.chat.id)
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data_tren:
            data_tren['trenerovka']['muscul'] = muscle_ru

def fetch_rows(message: Message, muscle_en, muscle_ru, case_number):
    """
    Функция вывода сообщений пользователю по 5 строк с таблицы  trenirovka
    :param muscle_ru: наименование группы мышц
    :param case_number: первая строка для вывода в сообщении
    :return:
    """
    if case_number == 5:
        keyboard = keyboard_trenerovka_id_2()
    else:
        keyboard = keyboard_trenerovka_id()
    list_trenerovok = muscle_record_check(muscle_en, muscle_ru, message, case_number)
    bot.send_message(message.chat.id, f'Выберите один из предложенных упражнений, '
                                      f'и напишите мне номер упражнения. Я Вам выведу отдельно большее описание и видео '
                                      f'выполнения упражнения: \n\n {list_trenerovok} \n Ничего не понравилось? '
                                      f'Нажмите "ЕЩЕ", передумали и хотите выбрать другую мышцу нажмите "Назад" ',
                     reply_markup=keyboard)


@bot.message_handler(state=TrenerState.trenerovka_id)
def trenerovka_id_dir(message: Message):
    """
    Функция позволяющая выбрать пользователю необходимое упражнение
    :param message:
    :return: None
    """
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data_tren:
        muscle_ru = data_tren['trenerovka']['muscul']
        tranclator = Translator()
        muscle_en = tranclator.translate(muscle_ru, 'en', 'ru')

        if message.text == 'ЕЩЕ':
            fetch_rows(message,  muscle_en, muscle_ru, 5)
        elif message.text == "Далее":
            fetch_rows(message, muscle_en, muscle_ru, 10)
        elif message.text == 'НАЗАД':
            fetch_rows(message, muscle_en, muscle_ru, 0)
        else:
            bot.send_message(message.chat.id, f'Выберите один из предложенных упражнений, уровней интенсивности', reply_markup=keyboard_sets())
            bot.set_state(message.from_user.id, TrenerState.sets, message.chat.id)
            data_tren['trenerovka']['trenerovka_id']=message.text

@bot.message_handler(state=TrenerState.sets)
def trenerovka_sets_dir(message: Message):
    """
    Функция вывода пользователю информации по выбранным им параметрам
    :param message:
    :return: None
    """
    bot.send_message(message.chat.id, "Успешных тренеровок. Можете включить для себя видео с объяснением, как выполняются упражнения")
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data_tren:
        data_tren['trenerovka']['sets']=message.text
    save_trenerovka_dir(data_tren['trenerovka'])
    if data_tren['trenerovka']['sets'] == "Легкий":
        msg = "Выполните 3 подхода по 12-15 повторений"
    elif data_tren['trenerovka']['sets'] == "Средний":
        msg ="Выполните 4 подхода по 8 - 12 повторений"
    elif data_tren['trenerovka']['sets'] == "Тяжелый":
        msg ="Выполните 5 подхода по 3 - 10 повторений"
    bot.send_message(message.chat.id, f"{msg} \n {trenerovka(data_tren['trenerovka']['trenerovka_id'])}", reply_markup=keyboard_start())
    bot.delete_state(message.from_user.id,message.chat.id)