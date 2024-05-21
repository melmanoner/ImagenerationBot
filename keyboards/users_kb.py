from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

get_pic_btn = KeyboardButton('Отправить запрос')

user_kb = ReplyKeyboardMarkup()
user_kb.add(get_pic_btn)