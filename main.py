# main.py
import db # мой модуль для БД
import telebot # pip install pyTelegramBotAPI
from telebot import types
import markup # мой модуль клавиатур

TOKEN = ""

bot = telebot.TeleBot(TOKEN)

database = db.DataBase()

ADMIN = [1217864060, 1]

####################################################   команды
# /reg
@bot.message_handler(commands=['reg'])
def register(message):
    print(message)
    id = message.from_user.id
    username = message.from_user.username
    if database.select_user(id) is None: # если пользователя нет в БД
        database.add_user(id,username,0)
        bot.send_message(id, "Успешная регистрация")
    else:
        bot.send_message(id, "Вы уже зарегистрированы")



####################################################   текст

@bot.message_handler(content_types=['text','sticker'])
def text_handler(message):

    id = message.from_user.id
    username = message.from_user.username

  

    if message.content_type == 'text':
        if database.select_user(id) is None: # если пользователя нет в БД
            database.add_user(id,username,0)
            bot.send_message(id, "Успешная регистрация")



                #    (1,)    (0,)   в ответе получаю кортеж
        if database.check_ban_user(id)[0] == 1: # пользователь забанен
            bot.send_message(id, "Вы забанены))))")
            return # выхожу из функции

        if message.text == 'админ' and id in ADMIN:                                        # отправляю клавиатуру
            bot.send_message(id, "Приветствую администратора", reply_markup=markup.keyboard_admin)

        # рассылка_Всем доброе утро
        elif message.text.startswith('рассылка_') and id in ADMIN: #######################    рассылка
            text = message.text[9:] # беру текст без 'рассылка_'

            users = database.select_all_user()  # [(1, 'pavel', 0), (2, 'oleg', 0), (3, 'olga', 0), (4, 'alex', 0)]

            for user in users: # прохожусь по списку
                try: # пытаюсь отослать сообщение
                    bot.send_message(user[0], f"{text}")
                except: # если пользователя такого нет
                    print(user[0],"нет")

        #общий чат 
        elif message.text.startswith('-') : 
            text = message.text[1:] # беру текст без '-'

            users = database.select_all_user()  # [(1, 'pavel', 0), (2, 'oleg', 0), (3, 'olga', 0), (4, 'alex', 0)]

            for user in users: # прохожусь по списку
                try: # пытаюсь отослать сообщение
                    bot.send_message(user[0], f"{id} {username}: {text}")
                    # bot.send_message(user[0], f"{text}")# анонимный вариант

                except: # если пользователя такого нет
                    print(user[0],"нет")


    if message.content_type == 'sticker':
        sticker = message.sticker.file_id
    
        users = database.select_all_user()  # [(1, 'pavel', 0), (2, 'oleg', 0), (3, 'olga', 0), (4, 'alex', 0)]
        for user in users: # прохожусь по списку
            try: # пытаюсь отослать сообщение
                bot.send_sticker(user[0],sticker)

                # bot.send_message(user[0], f"{text}")# анонимный вариант
            except: # если пользователя такого нет
                print(user[0],"нет")



####################################################   обрабатываю callback
@bot.callback_query_handler(func= lambda call: True)
def callback_handler(call):
    id = call.id 
    if call.data == 'all_user':

        users = database.select_all_user()  # [(1, 'pavel', 0), (2, 'oleg', 0), (3, 'olga', 0), (4, 'alex', 0)]

        # 1  создание клавиатуры
        keyboard_all_user = types.InlineKeyboardMarkup() 

        for user in users: # прохожусь по списку
            # 2  создание кнопок
            user_btn = types.InlineKeyboardButton(text=f"id : {user[0]} - username : {user[1]}",
                                                   url = f'https://t.me/{user[1]}') # переходим в лс пользователя

            # 3  добавление кнопок в клавиатуру
            keyboard_all_user.add(
                user_btn
            )


        bot.send_message(call.from_user.id, "все пользователи", reply_markup=keyboard_all_user)


#################################################################  бан


    elif call.data == 'ban_user':
        users = database.select_all_user()  # [(1, 'pavel', 0), (2, 'oleg', 0), (3, 'olga', 0), (4, 'alex', 0)]

        # 1  создание клавиатуры
        keyboard_ban_user = types.InlineKeyboardMarkup() 

        for user in users: # прохожусь по списку
            # 2  создание кнопок
            ban_btn = types.InlineKeyboardButton(text=f"id : {user[0]} - username : {user[1]}",
                                                   callback_data=f'ban_{user[0]}')  # ban_1234

            # 3  добавление кнопок в клавиатуру
            keyboard_ban_user.add(
                ban_btn
            )


        bot.send_message(call.from_user.id, "выберите пользователя для бана", reply_markup=keyboard_ban_user)

    # ловлю пользователя для бана
    elif call.data.startswith("ban_"):
        id_ban = call.data[4:] # извлекаю id 
        database.ban_user(id_ban)
        bot.send_message(call.from_user.id, f"Пользователь {id_ban} забанен!")

#################################################################  разбан

    elif call.data == 'unban_user':
        users = database.select_all_user()  # [(1, 'pavel', 0), (2, 'oleg', 0), (3, 'olga', 0), (4, 'alex', 0)]

        # 1  создание клавиатуры
        keyboard_unban_user = types.InlineKeyboardMarkup() 

        for user in users: # прохожусь по списку
            # 2  создание кнопок
            unban_btn = types.InlineKeyboardButton(text=f"id : {user[0]} - username : {user[1]}",
                                                   callback_data=f'unban_{user[0]}')  # ban_1234

            # 3  добавление кнопок в клавиатуру
            keyboard_unban_user.add(
                unban_btn
            )


        bot.send_message(call.from_user.id, "выберите пользователя для разбана", reply_markup=keyboard_unban_user)

    # ловлю пользователя для бана
    elif call.data.startswith("unban_"):
        id_ban = call.data[6:] # извлекаю id 
        database.unban_user(id_ban)
        bot.send_message(call.from_user.id, f"Пользователь {id_ban} разбанен!")

# цикл бота
bot.polling()








