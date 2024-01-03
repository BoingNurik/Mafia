import time
from bot import dp, bot
from inkb import join_kb
from aiogram import types, Dispatcher
import threading
    
class Game():
    chats = []
    

msg = None
l = None
i = 0
s = 15

def timer():
    global msg,s
    while s > 0:
        s-=1
        print(s)
        time.sleep(1)

   
async def bot_start(message: types.Message):
    global l, i, msg
    
    x = False
    for i in range(len(Game.chats)):
        x = str(message.chat.id) in Game.chats[i][0]
        if x == True:
            break
    if message.from_user.id != message.chat.id and x == False:
        msg = await message.answer('Началась регистрация в игру', reply_markup=join_kb)
        l = str(message.chat.id), True, [], []
        Game.chats.append(l)
        print(Game.chats)
        threading.Timer(0, timer).start()
    elif message.from_user.id != message.chat.id and x != False and Game.chats[i][1] == False:
        await message.answer('Началась регистрация в игру', reply_markup=join_kb)
        x = [str(Game.chats[i][0])]
        Game.chats[i] = x[0], True, [], []
        threading.Timer(0, timer).start()
        print(Game.chats[i])
    elif message.from_user.id != message.chat.id and x != False and Game.chats[i][1] != False:
        await bot.send_message(message.chat.id, "в группе игра уже начата")
    else:
        await message.answer("Пиши команду в группе")
    await message.delete()
    
async def joinGame(message: types.Message):
    global l, i
    x = False

    if len(Game.chats[i][2]) == 0:
        await message.answer("Ты присоеденился в игру")
        l = [str(Game.chats[i][0]), True, [str(message.from_user.id)], [message.from_user.full_name]]
        Game.chats[i] = tuple(l)
        print(Game.chats)
        await bot.edit_message_text(f"<b>Присоеденились в игру:</b>\n{message.from_user.full_name}\n\n\n\n<b>Количество игроков: {len(Game.chats[i][2])}</b>",
                                    Game.chats[i][0],
                                    parse_mode='html',
                                    message_id=msg.message_id,
                                    reply_markup=join_kb)
    else:
        for n in range(len(Game.chats[i][2])):
            x = str(message.from_user.id) in Game.chats[i][2][n]
            if x:
                await message.answer("Добро пожаловать в бот")
                break
        if x == False: 
            await message.answer("Ты присоеденился в игру")
            l = list(Game.chats[i][2]).append(message.from_user.id), list(Game.chats[i][2]).append(message.from_user.full_name)
            Game.chats[i][2:3] = l
            await bot.edit_message_text(f"<b>Присоеденились в игру:</b>\n{message.from_user.full_name}\n\n\n\n<b>Количество игроков: {len(Game.chats[i][2])}</b>",
                                    Game.chats[i][0],
                                    parse_mode='html',
                                    message_id=msg.message_id,
                                    reply_markup=join_kb)
    
async def Cancel(message: types.Message):
    global i
    if message.from_user.id == message.chat.id:
        await message.answer("Пишите команду в группе")
    else:
        x = [str(Game.chats[i][0])]
        Game.chats[i] = x[0], False
        print(Game.chats[i])
        await message.answer("Игра отменена")
        await message.delete()



def register_handlers_players(dp : Dispatcher):
    dp.register_message_handler(bot_start, commands='game')
    dp.register_message_handler(joinGame, commands='start')
    dp.register_message_handler(Cancel, commands='cancel')
    
   
    