from loader import bot
from states.user_states import UserState
from telebot.types import Message
from keyboards.reply import keyboard_start
from database.command import save_request_people

@bot.message_handler(commands='change_people')
def change_get(message:Message):
    new_user(message)

@bot.message_handler(state=UserState.people)
def new_user(message: Message):
    user_id = message.from_user.id

    bot.set_state(message.from_user.id, UserState.weight, message.chat.id)
    bot.send_message(user_id, "Напиши свой вес:")

    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data['people'] = {'people': user_id}
        print(data['people'])


@bot.message_handler(state=UserState.weight)
def weight_get(message: Message):
    weight = message.text
    try:
        weight = int(weight)
    except ValueError:
        bot.send_message(message.chat.id, 'Введите вашу массу целым числом, в промежутке от 20 до 200 кг.')
        new_user(message)
    if weight < 20 or weight > 200:
        bot.send_message(message.chat.id, 'Извините, но масса человека не может быть таким. \n '
                                          'Введите вашу массу целым числом, в промежутке от 20 до 200 кг.')
        new_user(message)
    else:
        bot.set_state(message.from_user.id, UserState.height, message.chat.id)
        bot.send_message(message.chat.id, f'Введите Ваш рост:')
        with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
            data['people']['weight'] = weight


@bot.message_handler(state=UserState.height)
def height_get(message: Message):
    height = message.text
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        try:
            height = int(height)
        except ValueError:
            bot.send_message(message.chat.id, 'Введите свой рост целым числом в мм, в промежутке от 130 до 250 мм.')
            message.text = data['people']['weight']
            weight_get(message)
        if height <130 or height > 250:
            bot.send_message(message.chat.id, 'Рост человека не может быть таким. \nВведите свой рост целым числом в мм, \nв промежутке от 130 до 250 мм.')
            message.text = data['people']['weight']
            weight_get(message)
        else:
            bot.send_message(message.chat.id, "Введите Ваш возраст")
            bot.set_state(message.from_user.id, UserState.age, message.chat.id)
            data['people']['height'] = message.text


@bot.message_handler(state=UserState.age)
def age_get(message: Message):
    age = message.text
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        try:
            age = int(age)
        except ValueError:
            bot.send_message(message.chat.id, 'Введите свой возраст целым числом, в промежутке от 0 до 100 лет, столько сколько Вам полных лет.')
            message.text = data['people']['height']
            height_get(message)
        if age < 0 or age > 100:
            bot.send_message(message.chat.id,
                             'Извините но возраст людей не может быть таким. Введите свой возраст целым числом, в промежутке от 0 до 100 лет, столько сколько Вам полных лет.')
            message.text = data['people']['height']
            height_get(message)
        else:
            bot.send_message(message.chat.id, "Введите Ваш пол")
            bot.set_state(message.from_user.id, UserState.gender, message.chat.id)
            data['people']['age'] = message.text


@bot.message_handler(state=UserState.gender)
def gender_get(message: Message):
    gender = message.text
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        if gender in ['муж', 'жен']:
            bot.send_message(message.chat.id, "Спасибо!")
            bot.set_state(message.from_user.id, UserState.all, message.chat.id)
            data['people']['gender'] = message.text
            msg = (f"{message.from_user.first_name} проверьте свои данные: \n"
                       f"Ваш вес: {data['people']['weight']} кг \n"
                       f"Ваш рост: {data['people']['height']} см \n"
                       f"Вам {data['people']['age']} лет \n"
                       f"Ваш пол: {data['people']['gender']}\n"
                       f"Если все верно, напишите"
                       )
            bot.send_message(message.chat.id, msg)
        else:
            message.text = data['people']['age']
            bot.send_message(message.chat.id, "Извините, но пол может быть либо мужским, либо женским. Если вы мужчина наберите 'муж', если женщина - 'жен' ")
            age_get(message)

@bot.message_handler(state=UserState.all)
def ready_for_answer(message: Message):
    all_data=message.text.title()
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data['people']["all"] = all_data
        if data['people']['all'] in ['Верно', 'Да', "Правильно"]:
            bot.send_message(message.chat.id, f" Замечательно. \n Сейчас выберите одно из дейсвтий:",
                             reply_markup=keyboard_start())
            people = data['people']
            print(people)
            save_request_people(people['people'], people['weight'],people['height'],people['age'], people['gender'])
            bot.delete_state(message.from_user.id, message.chat.id)
        else:
            bot.delete_state(message.from_user.id, message.chat.id)
            bot.send_message(message.chat.id, "Хорошо исправим.\n")
            new_user(message)




