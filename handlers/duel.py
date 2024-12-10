import random
from aiogram import Router, F
from aiogram.types import CallbackQuery
from keyboards.inline import get_duel_menu

router = Router()

player_health = 100
opponent_health = 100
player_points = 0

DUEL_ACTIONS = {
    "attack": "⚔️ Ви атакували!",
    "defend": "🛡️ Ви захистилися!",
    "special_attack": "⚡ Ви використали Спец. Атаку!"
}


@router.callback_query(F.data.in_(DUEL_ACTIONS.keys()))
async def duel_callback(callback: CallbackQuery):
    global player_health, opponent_health, player_points
    action = callback.data
    message = ""

    if action == "attack":
        damage = random.randint(15, 25)
        opponent_health -= damage
        player_points += 10
        message = (
            DUEL_ACTIONS[action] +
            f"\n⚔️ Ви завдали {damage} шкоди супротивнику." +
            f"\n🏆 Очки: {player_points}" +
            f"\nВаше здоров'я: {player_health}" +
            f"\nЗдоров'я супротивника: {opponent_health}"
        )

    elif action == "defend":
        reduced_damage = random.randint(5, 10)
        player_health -= max(0, reduced_damage - 5)
        message = (
            DUEL_ACTIONS[action] +
            f"\n🛡️ Ви зменшили шкоду до {reduced_damage}." +
            f"\nВаше здоров'я: {player_health}" +
            f"\nЗдоров'я супротивника: {opponent_health}"
        )
    elif action == "special_attack":
        player_health -= 10
        opponent_health -= 30
        player_points += 20
        message = (
            DUEL_ACTIONS[action] +
            f"\n⚡ Ви завдали 30 шкоди, але втратили 10 здоров'я." +
            f"\n🏆 Очки: {player_points}" +
            f"\nВаше здоров'я: {player_health}" +
            f"\nЗдоров'я супротивника: {opponent_health}"
        )

    if player_health <= 0:
        message += "\n💀 Ви програли дуель! Почніть нову гру."
        reset_game()
    elif opponent_health <= 0:
        message += "\n🏆 Ви перемогли дуель! Очки додаються до загального рахунку."
        reset_game()
    else:
        await callback.message.edit_text(message, reply_markup=get_duel_menu())

    await callback.answer()


@router.callback_query(F.data == "start_duel")
async def start_duel(callback: CallbackQuery):
    reset_game()
    await callback.message.edit_text("Дуель починається! Виберіть вашу дію:", reply_markup=get_duel_menu())
    await callback.answer()


def reset_game():
    global player_health, opponent_health
    player_health = 100
    opponent_health = 100
