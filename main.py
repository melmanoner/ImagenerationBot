from bot import dp, bot
from aiogram.utils import executor
from config import BOT_ADMIN
from handlers.users.user_handlers import register_handlers_users
from utils.database.create_tables import create_table


async def bot_start(_):
    bot_info = await bot.get_me()
    await bot.send_message(BOT_ADMIN, f'''Бот {bot_info['first_name']} запущен!▶''')

async def bot_stop(_):
    bot_info = await bot.get_me()
    await bot.send_message(BOT_ADMIN, f'''Бот {bot_info['first_name']} остановлен!🛑''')

register_handlers_users(dp)
create_table()

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True, on_startup=bot_start, on_shutdown=bot_stop)