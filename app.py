from data.config import ADMINS
from aiogram import executor

from loader import dp
import middlewares, filters, handlers
from utils.misc.logger import setup_logger
from utils.notify_admins import notify_admins
from utils.set_bot_commands import set_default_commands


async def on_startup(dispatcher):
    # Устанавливаем дефолтные команды
    await set_default_commands(dispatcher)

    # Уведомляет про запуск
    await notify_admins(ADMINS)
    
if __name__ == '__main__':
        setup_logger("INFO", ["sqlalchemy.engine", "aiogram.bot.api"])
        executor.start_polling(dp, on_startup=on_startup)
