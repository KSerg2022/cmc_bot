import requests
from pprint import pprint

from aiogram import Bot, Dispatcher, types, F, Router, flags
from aiogram.filters.command import Command
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Text
from aiogram.fsm.context import FSMContext

from keyboards.kb import kb_blockchain, kb_exit
from state.states import Gen
from utils.pretty_table import get_table

router = Router()

url = 'http://localhost:8000/'

blockchain_portfolio = 'api/bot/blockchain-portfolio/'  #  'api/bot/blockchain-portfolio/<str:tel_username>/'
blockchain_portfolio_data_for_user = 'api/bot/blockchain/data/'  #  api/bot/blockchain/data/<int:blockchain_id>/<str:tel_username>/


@router.message(Text("Blockchain"))
async def blockchain(message: types.Message, state: FSMContext):
    data = await get_blockchain(telegram_username=message.from_user.username)
    builder_kb = kb_blockchain(data)

    await state.set_state(Gen.blockchain)
    await message.answer('Choose, please, Blockchain?', reply_markup=builder_kb.as_markup())
    await message.answer('Чтобы выйти из диалога Blockchain нажмите на кнопку ниже', reply_markup=kb_exit)


async def get_blockchain(telegram_username):
    response = requests.get(f'{url}{blockchain_portfolio}{telegram_username}', auth=('Sergey', '!qa2ws3ed'))
    data = response.json()
    return data


@flags.chat_action("typing")
@router.callback_query(F.data, Gen.blockchain)
async def blockchain_data(clbck: CallbackQuery, state: FSMContext):
    data = await get_blockchain_data(blockchain_id=clbck.data, telegram_username=clbck.message.chat.username)
    builder_kb = kb_blockchain(await get_blockchain(telegram_username=clbck.message.chat.username))

    await clbck.message.answer(str(data), reply_markup=builder_kb.as_markup())


async def get_blockchain_data(blockchain_id, telegram_username):

    response = requests.get(f'{url}{blockchain_portfolio_data_for_user}{blockchain_id}/{telegram_username}',
                            auth=('Sergey', '!qa2ws3ed'))
    data = response.json()
    data = get_table(data)
    return f'<pre>{data}</pre>'

