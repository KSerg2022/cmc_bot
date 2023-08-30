"""Фильтры и мидлвари¶"""
import os
import asyncio
import logging

from aiogram import Bot, Dispatcher


from dotenv import load_dotenv

from handlers import group_games, usernames, checkin
from .middlewares.weekend import WeekendCallbackMiddleware

load_dotenv()

from config_reader import config


# Запуск процесса поллинга новых апдейтов
async def main():
    bot = Bot(token=config.bot_token.get_secret_value())
    dp = Dispatcher()

    dp.include_router(group_games.router)
    dp.include_router(usernames.router)
    dp.include_router(checkin.router)
    dp.callback_query.outer_middleware(WeekendCallbackMiddleware())

    # Запускаем бота и пропускаем все накопленные входящие
    # Да, этот метод можно вызвать даже если у вас поллинг
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
