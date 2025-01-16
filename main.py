from loader import bot
from telebot import custom_filters
from utils.set_default_commands import set_default_commands


if __name__ == "__main__":
    bot.add_custom_filter(custom_filters.StateFilter(bot))
    set_default_commands(bot)
    bot.infinity_polling()
