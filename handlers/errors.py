import logging
from aiogram import Router, types
from aiogram.exceptions import TelegramAPIError
from config import config

logger = logging.getLogger(__name__)
router = Router()


@router.errors()
async def handle_telegram_error(update: types.Update, error: TelegramAPIError):
    logger.error(f"Telegram API Error: {error}, update: {update}")

    await bot.send_message(
        config.ADMIN_ID,
        f"⚠️ Bot error:\n"
        f"Message text: {update.message.text if update.message else 'No text'}\n"
        f"User: @{update.message.from_user.username if update.message.from_user else 'Unknown'}\n"
        f"Error: {error}"
    )

    return True
