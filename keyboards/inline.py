from aiogram.utils.keyboard import InlineKeyboardBuilder


def get_magic_menu():
    kb = InlineKeyboardBuilder()
    kb.button(text="🔥 Вогняна куля", callback_data="fireball")
    kb.button(text="💊 Зцілення", callback_data="heal")
    kb.button(text="👻 Невидимість", callback_data="invisibility")
    kb.button(text="🔙 Повернутися в меню", callback_data="main_menu")
    kb.adjust(1)  # 1 кнопка в рядку
    return kb.as_markup()


def get_duel_menu():
    kb = InlineKeyboardBuilder()
    kb.button(text="⚔️ Атака", callback_data="attack")
    kb.button(text="🛡️ Захист", callback_data="defend")
    kb.button(text="⚡ Спец. Атака", callback_data="special_attack")
    kb.button(text="🔙 Повернутися в меню", callback_data="main_menu")
    kb.adjust(1)
    return kb.as_markup()


def get_main_menu():
    kb = InlineKeyboardBuilder()
    kb.button(text="🪄 Магічні дії", callback_data="magic_menu")
    kb.button(text="⚔️ Почати дуель", callback_data="start_duel")
    kb.adjust(1)
    return kb.as_markup()
