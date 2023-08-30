import requests
from pprint import pprint

from aiogram import Bot, Dispatcher, types, F, Router, flags
from aiogram.filters.command import Command
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Text
from aiogram.fsm.context import FSMContext


from utils.pretty_table import get_table_all_data

router = Router()

url = 'http://localhost:8000/'

all_data = 'api/user/data/all/'


@router.message(Text("All data"))
async def blockchain(message: types.Message):
    data = await get_all_data()
    await message.answer(str(data))


async def get_all_data():
    response = requests.get(f'{url}{all_data}', auth=('Sergey', '!qa2ws3ed'))
    data = response.json()
    data = get_table_all_data(data)
    return f'<pre>{data}</pre>'

