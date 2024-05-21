import asyncio

from aiogram import types, Dispatcher
from bot import bot
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
import requests
import json
import time
from utils.api_ai import Text2ImageAPI as ai
from config import AI_KEY
import base64
from utils.database.dbms import add_new_user, check_queue, add_to_queue, show_queue, add_new_queue, delete_queue, reset_queue
from keyboards.users_kb import user_kb

class WaitingInLine(StatesGroup):
    get_a_number = State()
    get_a_picture = State()



async def command_start(message:types.Message):
    #reset_queue()
    print(show_queue())
    tg_id = message.from_user.id
    username = message.from_user.username
    first_name = message.from_user.first_name
    register_date = str(message.date.date())
    add_new_user(tg_id,username, first_name, register_date)
    await bot.send_message(tg_id, f'''Привет, {first_name}!''')



async def get_in_line(callback_query:types.CallbackQuery):
    #await state.update_data(request = message.text)
    queue = int(check_queue()[0])
    queue_up = queue+1
    add_to_queue(queue_up)
    waiting_time = queue_up*40/60
    await bot.send_message(callback_query.from_user.id,
                           f'''Ваша позиция в очереди: {queue_up}\nПримерное время ожидания {round(waiting_time, 2)} минут. Пожалуйста подождите ⏳''')

    await bot.send_message(callback_query.from_user.id, '''Введите ваш запрос: ''')
    #await bot.send_message(callback_query.from_user.id, f'''Ваша позиция в очереди: {queue_up}\nПримерное время ожидания {round(waiting_time, 2)} минут. Пожалуйста подождите ⏳''')

    await WaitingInLine.get_a_picture.set()
    #try:
    #    async with asyncio.Lock():
    #        await gen_pic(message.text, message.from_user.id)
    #except Exception as e:
    #    print(e)




async def gen_pic(message:types.Message):
    queue = int(check_queue()[0])
    queue_up = queue + 1
    add_to_queue(queue_up)
    waiting_time = queue_up * 40 / 60
    await bot.send_message(message.from_user.id,
                           f'''Ваша позиция в очереди: {queue_up}\nПримерное время ожидания {round(waiting_time, 2)} минут. Пожалуйста подождите ⏳''')
    download_message = await bot.send_message(message.from_user.id, 'Загузка...')
    api = ai('https://api-key.fusionbrain.ai/', 'D4E08573C8C56757095C56928FF0479B', AI_KEY)
    model_id = api.get_model()
    #data = await state.get_data()
    #request = data['request']
    #request = message.text
    print(message.text)
    uuid = api.generate(f'''{message.text}''', model_id)
    images = api.check_generation(uuid)
    image_base64 = images[0]
    image_data = base64.b64decode(image_base64)
    with open("image.jpg", "wb") as file:
        file.write(image_data)
    await download_message.delete()
    await bot.send_photo(message.from_user.id, open('image.jpg', 'rb'))
    queue = check_queue()[0]
    new_queue = queue-1
    add_to_queue(new_queue)
    #await state.finish()


def register_handlers_users(dp: Dispatcher):
    dp.register_message_handler(command_start, commands='start')
    #dp.register_message_handler(get_in_line,content_types=['text'], text='Отправить запрос')
    dp.register_message_handler(gen_pic, content_types=['text'])