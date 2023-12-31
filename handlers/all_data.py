import os

import requests
from pprint import pprint

from aiogram import Bot, Dispatcher, types, F, Router, flags
from aiogram.filters.command import Command
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Text
from aiogram.fsm.context import FSMContext


from utils.pretty_table import get_table_all_data

router = Router()

# url = 'http://localhost:8000/'
url = 'http://web-cmc:8000/'

all_data = 'api/bot/data-all/'  #  'api/bot/data-all/<str:tel_username>/'


@router.message(Text("All data"))
async def blockchain(message: types.Message):
    tables = await get_all_data(telegram_username=message.from_user.username,
                                chat_id=message.chat.id)

    await message.answer(f'Total amount: {len(tables)}')
    for name, table in tables.items():
        await message.answer(str(table))
    await message.answer('All tables printed.')


async def get_all_data(telegram_username, chat_id):
    headers = {'TEL-USERNAME': telegram_username,
               'BOT-NAME': os.environ.get('BOTNAME'),
               'USER-NAME': os.environ.get('USERNAME'),
               'CHAT-ID': str(chat_id),
               }
    response = requests.get(f'{url}{all_data}',
                            headers=headers)
    data = response.json()
    tables = get_table_all_data(data)
    return tables

