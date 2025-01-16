from loader import bot
from telebot.types import Message
from handlers.custom_handlers.new_users import new_user
import sqlite3 as sq
from database.command import save_request_user
from database import health_life
from keyboards.reply import keyboard_start

def step(message: Message) -> None:
    user_id = message.from_user.id
    user_name = message.from_user.username
    first_name = message.from_user.first_name
    with health_life:
        health_life.row_factory = sq.Row
        list_id = health_life.execute(f"SELECT `user_id` FROM `users`")
        print(list_id)
        for res in list_id:
            print(res['user_id'], '', user_id)
            if user_id != list_id:
                bot.send_message(message.chat.id,
                                 f"Добро пожаловать {first_name}! \n Выберите один из команд, в пункте меню",
                                 reply_markup=keyboard_start())
                return
            else:
                bot.send_message(message.chat.id,
                                 'Добро пожаловать! Вы ранее с нами не тренировались. Поэтому мне нужно знать ваш рост, вес ... '
                                 'Для сравнения результатов в дальнейшем')
                save_request_user(user_id, user_name, first_name)
                new_user(message)

    # if users.get_or_none(users.user_id == user_id) is None:
    #     users.create(user_id=user_id, user_name=user_name, first_name=first_name)
    #     bot.send_message(message.chat.id, "Для начала мне нужно уточнить Ваш вес, рост, возраст ... \n Начнем?")
    #     bot.set_state(message.from_user.id, UserState.people, message.chat.id)
    #     new_user(message)
    # else:
    #     bot.send_message(message.chat.id, f"Добро пожаловать {first_name}! \n Выберите один из команд, в пункте меню")
    #     set_default_commands(bot)