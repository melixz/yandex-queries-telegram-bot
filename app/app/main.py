import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import BotCommand
from aiogram.fsm.storage.memory import MemoryStorage
from handlers import commands
from core.config import TELEGRAM_TOKEN


async def main():
    if not TELEGRAM_TOKEN:
        raise ValueError("TELEGRAM_TOKEN must be set")

    bot = Bot(token=TELEGRAM_TOKEN)
    dp = Dispatcher(storage=MemoryStorage())

    dp.include_router(commands.router)

    await bot.set_my_commands(
        [
            BotCommand(
                command="top_views", description="Топ-10 запросов по просмотрам"
            ),
            BotCommand(command="top_clicks", description="Топ-10 запросов по кликам"),
            BotCommand(command="top_ctr", description="Топ-10 запросов по CTR"),
        ]
    )

    try:
        print("Бот запущен!")
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(main())
