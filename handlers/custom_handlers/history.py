from loader import bot
from database.command import user_request_history, trenerovka
from states.user_states import HistoryState
from keyboards.reply import keyboard_start

from telebot.types import Message

@bot.message_handler(state='*', commands=['history'])
def handler_history(message: Message):
    history = user_request_history(message.from_user.id)
    bot.send_message(message.chat.id, f'{history} \n Наберите номер упражнения и я вам отправлю текст  и видео выполнения упражнения')
    bot.set_state(message.from_user.id, HistoryState.trenerovka_id, message.chat.id)
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data_history:
        data_history['history'] = {'user_id': message.from_user.id}

@bot.message_handler(state=HistoryState.trenerovka_id)
def history_get(message: Message):
    trenerovka_id = message.text
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data_history:
        data_history['history'] ={'trenerovka_id':trenerovka_id}
    result = trenerovka(trenerovka_id)
    bot.send_message(message.chat.id, result, reply_markup=keyboard_start())
    bot.delete_state(message.from_user.id, message.chat.id)
