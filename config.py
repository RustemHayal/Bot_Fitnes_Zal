import os
from dotenv import load_dotenv, find_dotenv

if not (p := find_dotenv()):
    exit('Переменные окружения не загружены т.к отсутствует файл .env')
else:
    load_dotenv(dotenv_path=p)

BOT_TOKEN = os.getenv('BOT_TOKEN')
RAPID_API_KEY = os.getenv('RAPID_API_KEY')
COMMANDS = (
    ('start', "Запустить бота"),
    ('help', "Вывести справку"),
    ('change_people', 'изменить массу, рост, вес ... '),
    ('trenerovka', 'тренировки'),
    ('history', 'история поиска'),
    ('challenging_workouts', 'вывести просмотренные последние 5 усложненных тренировок'),
    ('average_workouts', 'вывести просмотренные последние 5 тренировок средней сложностей'),
    ('easy_workouts', 'вывести просмотренные последние 5 легких тренировок'),
    ('cancel', 'Выйти. Завершить сеанс.')
)

NUMBER_OF_FOTO = 7  # количество выводимых фото по умолчанию
DES_TO_FILE = True  # запись запроса уточнения локации в файл
FOTO_TO_FILE = True  # запись запросов фото в файл
RESPONSE_FROM_FILE = True  # попытка считать ответ из файла, если подходящий есть в базе (только для FOTO и DES)

HISTORY = 5  # Количество запросов выводимых в истории
datab = 'history.db'
muscles_list = {
        'Бицепс': 'Biceps', 'Трицепс': 'Triceps', 'Грудь': 'Chest', 'Назад': 'Back',
        'Ноги': 'Legs', 'пресс': 'Abs', 'Растяжка': 'Stretching', 'Разогревать': 'Warm Up',
        'лат': 'Lats', 'Подколенное сухожилие': 'Hamstring', 'Телята': 'Calves', 'квадрицепсы': 'Quadriceps',
        'Трапеция': 'Trapezius', 'Плечи': 'Shoulders', 'Ягодицы': 'Glutes'
}
muscl_ru=[
        'Бицепс', 'Трицепс', 'Грудь', 'Назад', 'Ноги', 'пресс', 'Растяжка', 'Разогревать',
        'лат', 'Подколенное сухожилие', 'Телята', 'квадрицепс', 'Трапеция', 'Плечи', 'Ягодицы'
]