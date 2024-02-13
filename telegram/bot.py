import asyncio
from aiogram import Bot, Dispatcher
from config_data.config import config
from handlers import user_handlers


# Функция конфигурирования и запуска бота
async def main():

    # Инициализируем бот и диспетчер
    bot = Bot(token=config.tg_bot.token)
    # storage = MemoryStorage()
    dp = Dispatcher()

    # Регистриуем роутеры в диспетчере
    dp.include_router(user_handlers.router)

    # Пропускаем накопившиеся апдейты и запускаем polling
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
