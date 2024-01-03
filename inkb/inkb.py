from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

x = InlineKeyboardButton("Присоеденится к игре", url='https://t.me/MBFN_bot?start=join')
join_kb = InlineKeyboardMarkup()
join_kb.add(x)