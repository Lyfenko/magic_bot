import logging
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import Update
from aiogram.exceptions import TelegramAPIError
from aiogram.client.default import DefaultBotProperties

from config import config
from handlers import start, magic, duel, errors

# Налаштування логування
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("logs/bot.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# Ініціалізація бота
bot_properties = DefaultBotProperties(parse_mode="HTML")  # Use DefaultBotProperties for configuration
bot = Bot(token=config.BOT_TOKEN, default=bot_properties)
dp = Dispatcher(storage=MemoryStorage())

# Реєстрація обробників
dp.include_router(start.router)
dp.include_router(magic.router)
dp.include_router(duel.router)
dp.include_router(errors.router)


# Глобальний обробник помилок
@dp.error()
async def global_error_handler(update: Update, exception: Exception):
    """Обробка будь-яких необроблених помилок"""
    if isinstance(exception, TelegramAPIError):
        logger.warning(f"Помилка Telegram API: {exception}")
    else:
        logger.error(f"Неочікувана помилка: {exception}", exc_info=True)

    # Відправити повідомлення адміністратору
    await bot.send_message(
        config.ADMIN_ID,
        f"⚠️ Помилка в роботі бота:\n{exception}"
    )

    return True


# Запуск бота
async def main():
    logger.info("Бот запущено...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
