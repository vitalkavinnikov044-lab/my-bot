import logging
import asyncio
import sys
from aiogram import Bot, Dispatcher, types

# Твой токен и список модераторов
API_TOKEN = '8073761046:AAFcUhzGeoq03Eto-e7GBohAP-UX-TmEVpI'
MODERATOR_USERNAMES = ["AgushyNadaKyshat", "MegaladonGo"]

logging.basicConfig(level=logging.INFO, stream=sys.stdout)

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

@dp.message()
async def echo(message: types.Message):
    if message.from_user.username in MODERATOR_USERNAMES:
        await message.answer(f"🚀 Бот запущен на Koyeb! Привет, {message.from_user.username}!")
    else:
        await message.answer("Доступ ограничен.")

async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())


