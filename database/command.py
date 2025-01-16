from . import health_life
from loader import bot
from utils.api_trener import get_trenerovka

from telebot.types import Message
import datetime
import sqlite3


def save_request_user(user_id, user_name, first_name) -> None:
    """
    Функция проверяет на наличие данных и\или сохраняет данные пользователя.
    :return: None
    """

    with health_life:
        health_life.execute("""
        INSERT INTO  users (user_id, user_name, first_name) 
        VALUES(?,?,?)""",
                            (user_id, user_name, first_name))

def save_request_people(user_id, weight, height, age, gender) -> None:
    """
    Функция сохраняет данные пользователя.
    :return: None
    """
    today_now = datetime.date.today()
    with health_life:
        health_life.execute("""INSERT INTO  people (user_id, weight, height, age, gender, datetime) 
        VALUES(?, ?, ?, ?, ?, ?)""", (user_id, weight, height, age, gender, today_now))


def history_save_user(user_id, message: Message):
    """
    Функция проверяет пользователя, был ли он ранее зарегистрирован
    :param user_id: id номер пользователя в телеграмм
    :param message: область текущего сообщения
    :return: Bool
    """
    with health_life:
        health_life.row_factory = sqlite3.Row
        id_list = health_life.execute("""SELECT `user_id` FROM `users`""")
        for res in id_list:
            if user_id != res['user_id']:
                bot.reply_to(message, 'Вы не были зарегистрированы. Напишите \start')
                return True
            else:
                bot.send_message(message.chat.id, f'Добрый день {message.from_user.first_name}!')
                return False


def save_trenerovka_of_muscless(user_id, muscless, equipment, explaination, long_explanation, video):
    """
    Функция сохранения в таблицу данных о упражнениях для тренеровок из API
    :param user_id: id номер в телеграмме
    :param muscless: мускулы, на которые делается упражнения
    :param equipment: упражнение
    :param explaination: краткое описание
    :param long_explanation: описание
    :param video: видео
    :return: None
    """
    with health_life:
        health_life.execute("""INSERT INTO trenerovka (user_id, muscless, equipment, explaination, long_explanation, video)
        VALUES(?, ?, ?, ?, ?, ?)""", (user_id, muscless, equipment, explaination, long_explanation, video))


def muscle_record_check(muscle_en, muscle_ru, message, number_list):
    """
    Функция возвращающая лист с 5-ью различными способами, краткими описаниями тренировок
    :param muscle_en: наименование мускула на английском языке
    :param muscle_ru: наименование мускула на русском языке
    :param message: сообщения
    :param number_list: порядковый номер описания тренировок, с которого начинается лист
    :return: список тренировок
    """
    with health_life:
        health_life.row_factory = sqlite3.Row
        muscle_list = health_life.execute("""SELECT `muscless` FROM `trenerovka`""")
        try:
            for muscle in muscle_list:
                if muscle_ru == muscle['muscless']:
                        record = health_life.execute(f"""SELECT `req_id`, `explaination` 
                                                        FROM `trenerovka` WHERE `muscless` = 
                                                        \"{muscle_ru}\" LIMIT 5 OFFSET {number_list}""").fetchall()
                trenerov = str()
            for rec in record:
                trenerov = trenerov + f"{rec[0]}. {rec[1]} \n \n"
            return trenerov
        except UnboundLocalError:
            bot.send_message(message.chat.id, 'Минуточку, я ищу для Вас упраженния в сети - Интернет')
            get_trenerovka(muscle_ru, message)
            muscle_record_check(muscle_en, muscle_ru, message, number_list)

def save_trenerovka_dir(trenerovka):
    """
    Функция сохранения данных в таблицу history.
    :param trenerovka: Информация собранная по TrenerState
    :return: None
    """
    with health_life:
        health_life.execute("""INSERT INTO history (user_id, muscless, trenerovka_id, sets, date) VALUES (?, ?, ?, ?, ?)
        """, (trenerovka['trenerovka'], trenerovka['muscul'], trenerovka['trenerovka_id'], trenerovka['sets'], datetime.datetime.now()))

def trenerovka(trenerovka_id):
    """
    Функция вывода строки из таблицы trenerovka пользователю по выбранным им параметрам по TrenerState
    :param trenerovka: Информация собранная по TrenerState
    :return: подробное описание упраженения и видео для самообучения
    """
    with health_life:
        health_life.row_factory = sqlite3.Row
        trenerov = health_life.execute(f"""SELECT `long_explanation`, `video`, `explaination` FROM `trenerovka` WHERE `req_id` = {trenerovka_id}""").fetchall()
    for res in trenerov:
        result = f"\n {res['long_explanation']}\n\n {res['explaination']} \n\n{res['video']}"
    return result

def max_trenerovka_id():
    with health_life:
        health_life.row_factory = sqlite3.Row
        max_id = health_life.execute("SELECT MAX(`req_id`) FROM `trenerovka`").fetchall()
    for max in max_id:
        max = str(max)
        max_id = max['req_id']

    return max_id

def user_request_history(user_id):
    """
    Функция выборки 5 последних просмотренных упражнений для тренировок
    :param user_id: id пользователя по телеграм каналу
    :return: список 5 последних тренировок
    """
    result = "\n Здесь последние 5 сохраненных тренировок \n"
    with health_life:
        health_life.row_factory = sqlite3.Row
        trener_list = health_life.execute(f"""SELECT muscless, trenerovka_id, sets, date FROM history WHERE user_id = {user_id} ORDER BY date DESC LIMIT 5""").fetchall()
    for trenerov in trener_list:
        result=str(result)
        result = f"{trenerov['trenerovka_id']} {trenerov['muscless']} {trenerov['sets']} {trenerov['date']} \n" + result
    return result


def request_chelinging_workout(user_id, workout):
    print(workout)
    result = "\n Здесь последние 5 сохраненных тренировок \n"
    with health_life:
        health_life.row_factory = sqlite3.Row
        trener_list = health_life.execute(f"""SELECT muscless, trenerovka_id, sets, date FROM history WHERE (sets = '{workout}' and user_id = {user_id}) ORDER BY date DESC LIMIT 5""").fetchall()
    for trenerov in trener_list:
        result = str(result)
        result = f"{trenerov['trenerovka_id']} {trenerov['muscless']} {trenerov['sets']} {trenerov['date']} \n" + result
    return result
