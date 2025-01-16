from loader import bot
from telebot.types import Message


@bot.message_handler(state="*", commands=['cancel'])
def handler_cancel(message: Message) -> None:
    bot.reply_to(message, "До новых встреч!")
    bot.delete_state(message.from_user.id, message.chat.id)
