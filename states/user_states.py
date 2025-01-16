from telebot.handler_backends import State, StatesGroup
from peewee import SqliteDatabase, Model, CharField, IntegerField
# from database import history


class UserState(StatesGroup):
    people = State()       # id ����� ������������
    weight = State()        # ��� ������������
    height = State()        # ���� ������������
    age = State()           # ������� ������������
    gender = State()        # ��� ������������
    all = State()           # ��� ���� ���������

class TrenerState(StatesGroup):
    muscul = State()            # �������, �� ������� ������ ����������
    sets = State()              # �������������, ��������
    trenerovka_id = State()     # ����� ����������

class HistoryState(StatesGroup):
    trenerovka_id = State()
    user_id = State()