from loader import bot
from telebot.types import Message
from handlers.custom_handlers.new_users import weight_get


def get_user_data(user_id, message) -> dict:
    with bot.retrieve_data(user_id) as data:
        res = data
        if not res:
            res = weight_get(message)

    return res

