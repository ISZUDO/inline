from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="bir bosishda o'ynang", callback_data='birinchi')
        ],
        [
            InlineKeyboardButton(text="Kanalimizga obuna bo'ling", url="https://t.me/hamster_kombat_bot")
        ],
        [
            InlineKeyboardButton(text="Qanday daromad olish mumkin?", callback_data='uchinchi')
        ],
    ]
)