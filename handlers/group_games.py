from aiogram import Router
from aiogram.enums.dice_emoji import DiceEmoji
from aiogram.types import Message
from aiogram.filters import Command

from mastergroosha.chapter5.filters.chat_type import ChatTypeFilter

router = Router()
router.message.filter(
    ChatTypeFilter(chat_type=["private", "group", "supergroup"])
)


@router.message(Command("dice"))
async def cmd_dice_in_group(message: Message):
    await message.answer_dice(emoji=DiceEmoji.DICE)


@router.message(Command("basketball"))
async def cmd_basketball_in_group(message: Message):
    await message.answer_dice(emoji=DiceEmoji.BASKETBALL)


# первый вариант
# router = Router()
#
# @router.message(
#     ChatTypeFilter(chat_type=["private", "group", "supergroup"]),
#     Command(commands=["dice"]),
# )
# async def cmd_dice_in_group(message: Message):
#     await message.answer_dice(emoji=DiceEmoji.DICE)
#
#
# @router.message(
#     ChatTypeFilter(chat_type=["private", "group", "supergroup"]),
#     Command(commands=["basketball"]),
# )
# async def cmd_basketball_in_group(message: Message):
#     await message.answer_dice(emoji=DiceEmoji.BASKETBALL)
