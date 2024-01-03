
from aiogram import types, Dispatcher
import random
import json, string



phrases = ["маты запрещены", "какой невоспитанный", "следи за языком", "физрук хорошо так постарался", "сам(-а) такой(-ая)", "хватить, а то по попе дам", "тише ты, а то админы придут", "ай-ай-ай", "тише ты, тут дети"]

#@dp.message_handler()
async def cenz(message: types.Message):
    msg = {i.lower().translate(str.maketrans('', '', string.punctuation)) for i in message.text.split(' ')}
    if msg.intersection(set(json.load(open("cenz.json")))) != set():
        await message.reply(random.choice(phrases))
        await message.delete()

async def start(message: types.Message):
    await message.answer("Добро пожаловать")
def register_handlers_other(dp : Dispatcher):
    dp.register_message_handler(start, commands="start")
    dp.register_message_handler(cenz)
