"""Фильтры и мидлвари¶"""
import os
import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.enums.parse_mode import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.utils.chat_action import ChatActionMiddleware

from dotenv import load_dotenv

load_dotenv()

from config_reader import config
from handlers import start, blockchain, exchanger, all_data, other


# Запуск процесса поллинга новых апдейтов
async def main():
    bot = Bot(token=config.bot_token.get_secret_value(), parse_mode=ParseMode.HTML)
    dp = Dispatcher(storage=MemoryStorage())

    dp.include_router(start.router)
    dp.include_router(blockchain.router)
    dp.include_router(exchanger.router)
    dp.include_router(all_data.router)
    dp.include_router(other.router)

    dp.message.middleware(ChatActionMiddleware())
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
