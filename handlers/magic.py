from aiogram import Router, F
from aiogram.types import CallbackQuery
from keyboards.inline import get_magic_menu

router = Router()

MAGIC_ACTIONS = {
    "fireball": "🔥 Ви викликали Вогняну кулю!",
    "heal": "💊 Ви зцілили себе!",
    "invisibility": "👻 Ви стали невидимим!"
}


@router.callback_query(F.data.in_(MAGIC_ACTIONS.keys()))
async def magic_callback(callback: CallbackQuery):
    magic_message = MAGIC_ACTIONS[callback.data]
    await callback.message.edit_text(magic_message)
    await callback.answer("Магія виконана! ✨")


@router.callback_query(F.data == "magic_menu")
async def show_magic_menu(callback: CallbackQuery):
    await callback.message.edit_text("Виберіть магічну дію:", reply_markup=get_magic_menu())
    await callback.answer()