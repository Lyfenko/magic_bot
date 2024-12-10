from aiogram import Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters.command import Command
from keyboards.inline import get_main_menu

router = Router()


@router.message(Command(commands=["start"]))
async def cmd_start(message: Message):
    await message.answer(
        "Виберіть дію:",
        reply_markup=get_main_menu()
    )


@router.callback_query(lambda callback: callback.data == "main_menu")
async def show_main_menu(callback: CallbackQuery):
    await callback.message.edit_text("Виберіть дію:", reply_markup=get_main_menu())
    await callback.answer("Повернення до головного меню")
