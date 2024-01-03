
from bot import dp
from aiogram.utils import executor







async def on_startup(_):
    print("Бот онлайн")

from handlers import players, other

players.register_handlers_players(dp)
#admin.register_handlers_admin(dp)
other.register_handlers_other(dp)




executor.start_polling(dp, skip_updates=True, on_startup=on_startup)