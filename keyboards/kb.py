from aiogram.types import (InlineKeyboardButton,
                           InlineKeyboardMarkup,
                           KeyboardButton,
                           ReplyKeyboardMarkup,
                           ReplyKeyboardRemove)

from aiogram.utils.keyboard import InlineKeyboardBuilder


menu = [
    [InlineKeyboardButton(text="📝 Генерировать текст", callback_data="generate_text"),
    InlineKeyboardButton(text="🖼 Генерировать изображение", callback_data="generate_image")],
    [InlineKeyboardButton(text="💳 Купить токены", callback_data="buy_tokens"),
    InlineKeyboardButton(text="💰 Баланс", callback_data="balance")],
    [InlineKeyboardButton(text="💎 Партнёрская программа", callback_data="ref"),
    InlineKeyboardButton(text="🎁 Бесплатные токены", callback_data="free_tokens")],
    [InlineKeyboardButton(text="🔎 Помощь", callback_data="help")]
]

menu = InlineKeyboardMarkup(inline_keyboard=menu)
# exit_kb = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="◀️ Выйти в меню")]], resize_keyboard=True)
iexit_kb = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="◀️ Выйти в меню", callback_data="menu")]])

###################

kb_start = ReplyKeyboardMarkup(input_field_placeholder="Choose ....",
                               resize_keyboard=True,
                               keyboard=[
                                   [KeyboardButton(text="Exchanger"),
                                    KeyboardButton(text="Blockchain"),
                                    KeyboardButton(text="All data")]]
                               )

kb_exit = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="◀️ Выйти в меню")]],
                              resize_keyboard=True)


def kb_blockchain(user_portfolios):
    builder_kb_blockchain = InlineKeyboardBuilder()
    for portfolio in user_portfolios['results']:
        builder_kb_blockchain.button(text=f'{portfolio["slug"].split("-")[-1].upper()}',
                                     callback_data=f'{portfolio["blockchain"]}'
                                     )
        builder_kb_blockchain.adjust(3)
    return builder_kb_blockchain


def kb_exchanger(user_portfolios):
    builder_kb_exchanger = InlineKeyboardBuilder()
    for portfolio in user_portfolios['results']:
        builder_kb_exchanger.button(text=f'{portfolio["slug"].split("-")[-1].upper()}',
                                    callback_data=f'{portfolio["exchanger"]}')
        builder_kb_exchanger.adjust(3)
    return builder_kb_exchanger


