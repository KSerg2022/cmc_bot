import requests

from aiogram import types, F, Router, flags
from aiogram.types import CallbackQuery
from aiogram.filters import Text
from aiogram.fsm.context import FSMContext

from keyboards.kb import kb_blockchain, kb_exit
from state.states import Gen
from utils.json_files.json_file import JsonFile
from utils.pretty_table import get_table

router = Router()

# url = 'http://localhost:8000/'
url = 'http://web-cmc:8000/'

blockchain_portfolio = 'api/bot/blockchain-portfolio/'
blockchain_portfolio_data = 'api/bot/blockchain-portfolio-data/'

json = JsonFile()





@router.message(Text("Blockchain"))
async def blockchain(message: types.Message, state: FSMContext):
    data = await get_blockchain(telegram_username=message.from_user.username)
    builder_kb = kb_blockchain(data)

    await state.set_state(Gen.blockchain)
    await message.answer('Choose, please, Blockchain?', reply_markup=builder_kb.as_markup())
    await message.answer('Чтобы выйти из диалога Blockchain нажмите на кнопку ниже', reply_markup=kb_exit)


# from requests.auth import AuthBase
# class BotAuth(AuthBase):
#     """Attaches HTTP Pizza Authentication to the given Request object."""
#     def __init__(self, tel_username):
#         self.username = tel_username
#
#     def __call__(self, r):
#         r.headers['Authorization'] = self.username
#         return r


async def get_blockchain(telegram_username):
    headers = {'TEL-USERNAME': telegram_username}
    response = requests.get(f'{url}{blockchain_portfolio}',
                            headers=headers,
                            )
    data = response.json()
    return data


@flags.chat_action("typing")
@router.callback_query(F.data, Gen.blockchain)
async def blockchain_data(clbck: CallbackQuery, state: FSMContext):
    data = await get_blockchain_data(blockchain_id=clbck.data, telegram_username=clbck.message.chat.username)
    builder_kb = kb_blockchain(await get_blockchain(telegram_username=clbck.message.chat.username))

    await clbck.message.answer(str(data), reply_markup=builder_kb.as_markup())


async def get_blockchain_data(blockchain_id, telegram_username):
    headers = {'TEL-USERNAME': telegram_username,
               'USER-PORTFOLIO-ID': blockchain_id}
    response = requests.get(f'{url}{blockchain_portfolio_data}',
                            headers=headers)
    data = response.json()
    data = get_table(data)
    return f'<pre>{data}</pre>'
