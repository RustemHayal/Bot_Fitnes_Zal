from telebot import TeleBot
from config import BOT_TOKEN
from telebot.storage import StateMemoryStorage


storage = StateMemoryStorage()
bot = TeleBot(token=BOT_TOKEN, state_storage=storage)