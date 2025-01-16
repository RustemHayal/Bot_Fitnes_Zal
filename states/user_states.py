from telebot.handler_backends import State, StatesGroup
from peewee import SqliteDatabase, Model, CharField, IntegerField
# from database import history


class UserState(StatesGroup):
    people = State()       # id номер пользователя
    weight = State()        # вес пользователя
    height = State()        # рост пользователя
    age = State()           # возраст пользователя
    gender = State()        # пол пользователя
    all = State()           # все поля заполнены

class TrenerState(StatesGroup):
    muscul = State()            # мускулы, на которые делает упражнения
    sets = State()              # интенсивность, нагрузка
    trenerovka_id = State()     # номер тренеровки

class HistoryState(StatesGroup):
    trenerovka_id = State()
    user_id = State()