import requests
from pprint import pprint


from aiogram import Bot, Dispatcher, types, F, Router, flags
from aiogram.filters.command import Command
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Text
from aiogram.fsm.context import FSMContext

from keyboards.kb import kb_exchanger, kb_exit
from state.states import Gen
from utils.pretty_table import get_table

router = Router()

url = 'http://localhost:8000/'

exchanger_list = 'api/exchanger'
exchanger_portfolio = 'api/exportfolio'
exchanger_portfolio_data_for_user = 'api/exchanger/data/'  #  'api/exchanger/data/<int:exchanger_id>/'


@router.message(F.text == "Exchanger")
async def exchanger(message: types.Message, state: FSMContext):
    data = await get_exchanger()
    builder_kb = kb_exchanger(data)

    await state.set_state(Gen.exchanger)
    await message.answer('Choose, please, Exchanger?', reply_markup=builder_kb.as_markup())
    await message.answer('Чтобы выйти из диалога с Exchanger нажмите на кнопку ниже', reply_markup=kb_exit)


async def get_exchanger():
    response = requests.get(f'{url}{exchanger_portfolio}', auth=('Sergey', '!qa2ws3ed'))
    data = response.json()
    return data


@flags.chat_action("typing")
@router.callback_query(F.data, Gen.exchanger)
async def exchanger_data(clbck: CallbackQuery, state: FSMContext):
    data = await get_exchanger_data(exchanger_id=clbck.data)
    builder_kb = kb_exchanger(await get_exchanger())

    await clbck.message.answer(str(data), reply_markup=builder_kb.as_markup())


async def get_exchanger_data(exchanger_id):
    response = requests.get(f'{url}{exchanger_portfolio_data_for_user}{exchanger_id}',
                            auth=('Sergey', '!qa2ws3ed'))
    data = response.json()
    data = get_table(data)
    return f'<pre>{data}</pre>'

