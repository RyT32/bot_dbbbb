#markup.py
from telebot import types

# 1  создание клавиатуры
keyboard_admin = types.InlineKeyboardMarkup() 

# 2  создание кнопок
adm_btn_1 = types.InlineKeyboardButton(text="all user", callback_data="all_user")
adm_btn_2 = types.InlineKeyboardButton(text="ban user", callback_data="ban_user")
adm_btn_3 = types.InlineKeyboardButton(text="unban user", callback_data="unban_user")





# 3  добавление кнопок в клавиатуру
keyboard_admin.add(
    adm_btn_1,
    adm_btn_2,
    adm_btn_3
)














