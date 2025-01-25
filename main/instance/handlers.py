import logging
import asyncio

from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery,InlineKeyboardMarkup, InlineKeyboardButton
# from main.models import client
from main.instance import utils
from main.instance.filters import TextFilter,StartsWithFilter
from aiogram.types import ContentType
from aiogram.filters import Filter as F

logging.basicConfig(level=logging.INFO)

webhook_dp = Dispatcher()
# async def handle_start(message: Message, bot: Bot) -> None:

    # bio = await request.get_first_bio()

    # await client.BotClient.create_or_update(
    #     chat_id=message.chat.id,
    #     first_name=message.from_user.first_name,
    #     last_name=message.from_user.last_name,
    #     username=message.from_user.username,
    #     language_code=message.from_user.language_code,
    # )
    # chat_id = message.chat.id
    # await bot.send_message(
    #     chat_id=chat_id,
    #     text=bio.name,
    #     reply_markup=await utils.get_lang_reply_markup()
    # )
    
    
    
# async def handle_language(callback_query: CallbackQuery, bot: Bot) -> None:
#     if callback_query.data.startswith("lang_"):
#         language_code = callback_query.data.split("_")[1]
#         await client.BotClient.change_language(
#             chat_id=callback_query.message.chat.id,
#             language_code=language_code
#         )
#         await Start.send_hello(
#             chat_id=callback_query.message.chat.id,
#             lang=language_code,
#             bot=bot
#         )
#         await callback_query.message.delete()
    









# webhook_dp.message.register(handle_start, CommandStart())
# webhook_dp.message.register(test1, TextFilter(text=["qalaysan566"]))
# webhook_dp.callback_query.register(handle_language, TextFilter(text=["lang_ru", "lang_en", "lang_uz"]))


async def feed_update(token: str, update: dict):

    try:
        webhook_book = Bot(token=token)
        aiogram_update = types.Update(**update)
        await webhook_dp.feed_update(bot=webhook_book, update=aiogram_update)
    finally:
        await webhook_book.session.close()
