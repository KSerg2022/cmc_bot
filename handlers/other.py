import requests
from aiogram import Bot, Dispatcher, types, F, Router
from aiogram.filters.command import Command
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Text
from pprint import pprint


router = Router()


@router.message(Text("id"))
async def message_handler(msg: Message):
    await msg.answer(f"Твой ID: {msg.from_user.id}")


@router.message()
async def echo_handler(message: types.Message) -> None:

    try:
        # pprint(message.__dict__)

        await message.send_copy(chat_id=message.chat.id)
        await message.answer('Не правильный выбор')

    except TypeError:
        # But not all the types is supported to be copied so need to handle it
        await message.answer("Nice try!")
