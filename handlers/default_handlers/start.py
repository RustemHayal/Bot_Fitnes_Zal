import handlers
from loader import bot
from telebot.types import Message
from states.user_states import UserState


@bot.message_handler(commands=['start'])
def handler_start(message: Message) -> None:
    """
    При первом включении, после нажатия команды /start, выводит приветсивенное сообщение
    """
    bot.send_message(message.chat.id,
                     f'Привет! Я бот. Могу помощь выбрать и правильно выполнять упражнения.'
                     )
    bot.send_message(message.chat.id, f'Вызов справки /help')
    bot.delete_state(message.from_user.id, message.chat.id)  # удаляем сохраненные данные
    handlers.custom_handlers.related.step(message)


