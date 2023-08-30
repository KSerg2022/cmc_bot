from aiogram.fsm.state import StatesGroup, State


class Gen(StatesGroup):
    blockchain = State()
    exchanger = State()
