from aiogram import Bot, Dispatcher, types, F, Router
from aiogram.filters.command import Command, CommandStart
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext

from keyboards.kb import kb_start

router = Router()


@router.message(CommandStart())
async def cmd_start(message: types.Message, state: FSMContext):
    await state.clear()
    await message.answer("Choose, please, Exchanger or Blockchain?", reply_markup=kb_start)


@router.message(F.text == "Меню")
@router.message(F.text == "Menu")
@router.message(F.text == "Выйти в меню")
@router.message(F.text == "◀️ Выйти в меню")
async def menu(message: Message, state: FSMContext):
    await state.clear()
    await message.answer('"📍 Главное меню"', reply_markup=kb_start)
