import asyncio
import os

from aiogram import Bot, Dispatcher, types
from dotenv import load_dotenv
from handlers import bot_handlers

load_dotenv()


async def main():
    bot = Bot(token=os.getenv('BOT_TOKEN'))
    dp = Dispatcher(bot=bot)

    dp.include_router(bot_handlers.router)

    try:
        print("Starting bot...")
        await bot.delete_webhook(drop_pending_updates=True)
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        print("Bot stopped!")
