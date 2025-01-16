import requests
from googletrans import Translator

from config import RAPID_API_KEY, muscles_list
from database import command
from telebot.types import Message

translator = Translator()
def get_trenerovka(muscl, message:Message):
    """
    Базовая функция запроса к API - Work Out API
    :param muscl: мускулы на которые направлены упражнения
    :param message: область сообщений с пользователем
    :return: None
    """
    print("API - save")
    if muscl in muscles_list:
        muscl = muscles_list[muscl]
    querystring = {"Muscles": muscl}
    url = "https://work-out-api1.p.rapidapi.com/search"
    headers = {
        "X-RapidAPI-Key": RAPID_API_KEY,
        "X-RapidAPI-Host": "work-out-api1.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)

    result = response.json()

    for trenerovka in result:
        trans_muscles = translator.translate(trenerovka['Muscles'], 'ru', 'en').text
        if trenerovka['Equipment'] != None:
            trans_Equipment = translator.translate(trenerovka['Equipment'], 'ru', 'en').text
        else:
            trans_Equipment = None
        if trenerovka['Explaination'] != None:
            trans_Explaination = translator.translate(trenerovka['Explaination'], 'ru', 'en').text
        else:
            trans_Explaination = None
        trans_Long_Explanation = translator.translate(trenerovka['Long Explanation'], 'ru', 'en').text
        command.save_trenerovka_of_muscless(message.from_user.id,
                                            trans_muscles,
                                            trans_Equipment,
                                            trans_Explaination,
                                            trans_Long_Explanation,
                                            trenerovka["Video"])
