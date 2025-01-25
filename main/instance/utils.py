import logging
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from main.instance.keyboards import build_keyboard

logging.basicConfig(level=logging.INFO)


async def get_lang_reply_markup():
    """
    Til tanlash uchun inline tugmalarini qaytaradi.

    Ushbu funksiya foydalanuvchiga ikki xil til variantini (Ruscha va O'zbekcha) tanlash imkonini beruvchi 
    inline klaviatura tugmalarini yaratadi.

    :return: InlineKeyboardMarkup obyekti, tilni tanlash uchun tugmalar bilan.
    """
    return await build_keyboard([
        [{'text': "🇷🇺 Русский", 'callback_data': "lang_ru"}],
        [{'text': "🇺🇿 O'zbekcha", 'callback_data': "lang_uz"}],
    ])


async def get_inline_keyboard(buttons_dict: dict) -> InlineKeyboardMarkup:
    """
    Inline klaviaturasi uchun tugmalarni yaratadi.
    Ushbu funksiya berilgan lug'atdagi har bir tugmani inline formatida klaviaturaga joylashtiradi.
    Har bir tugma uchun `text` (tugma matni) va `url` (tugmaga havola) qiymatlari olinadi.
    :param buttons_dict: Tugmalarni o'z ichiga olgan lug'at. Tugma matni (text) va havola (url) juftliklarini o'z ichiga oladi.
    :return: InlineKeyboardMarkup obyekti, tugmalar bilan to'ldirilgan klaviatura.
    """
    # Har bir button uchun InlineKeyboardButton yaratamiz va har bir tugmani alohida qatorga joylashtiramiz
    keyboard_data = [[InlineKeyboardButton(text=name, url=link)] for name, link in buttons_dict.items()]
    
    # Har bir tugmani yangi qatorda joylashtiramiz
    return InlineKeyboardMarkup(inline_keyboard=keyboard_data)

    

async def get_webapp_keyboard(buttons_dict: dict) -> InlineKeyboardMarkup:
    """
    Web ilovalariga bog'lanish uchun klaviatura yaratadi.

    Ushbu funksiya har bir tugma uchun matn va WebApp havolasini yaratadi, so'ngra bu tugmalarni
    `build_keyboard` funktsiyasiga yuborib, qayta formatlangan inline klaviatura hosil qiladi.

    :param buttons_dict: Tugmalarni o'z ichiga olgan lug'at. Tugma matni (text) va WebApp havolasi (web_app) juftliklarini o'z ichiga oladi.
    :return: InlineKeyboardMarkup obyekti, WebApp tugmalari bilan to'ldirilgan klaviatura.
    """
    # Convert the dictionary into the required format for build_keyboard
    keyboard_data = [{'text': name, 'web_app': link} for name, link in buttons_dict.items()]
    
    # Pass the formatted keyboard data to build_keyboard function
    return await build_keyboard([keyboard_data])



async def get_keyboard(lang: str, buttons: dict):
    """
    Foydalanuvchining tanlangan tiliga qarab klaviatura yaratadi.

    Ushbu funksiya foydalanuvchidan olingan tilga qarab, belgilangan tugmalarni tarjima qilib,
    inline klaviatura hosil qiladi. Tugmalar lug'ati va tilga qarab tegishli tarjimasi ishlatiladi.

    :param lang: Foydalanuvchining tanlangan tili ("ru" yoki "uz").
    :param buttons: Tugmalarni o'z ichiga olgan lug'at. Har bir tugma kalitlari (key) va uning matni tarjimasi kerak.
    :return: InlineKeyboardMarkup obyekti, foydalanuvchi uchun moslashtirilgan tugmalar bilan klaviatura.
    """
    translations = {
        "ru": {
            "start": "🚀 Начать",
        },
        "uz": {
            "start": "🚀 Boshlash",
        },
    }

    # Langga mos tarjimadan foydalanib, klaviatura yaratish
    keyboard = [
        [{'text': translations[lang][key], 'callback_data': f"{key}_{lang}"}] for key in buttons
    ]
    return await build_keyboard(keyboard)








