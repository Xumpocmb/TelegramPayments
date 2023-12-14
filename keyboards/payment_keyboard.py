from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def make_payment_keyboard(payment_link, payment_id):
    buttons = []
    button_payment = InlineKeyboardButton(text="Оплатить", url=payment_link)
    buttons.append(button_payment)
    button_check = InlineKeyboardButton(text="Проверить", callback_data=payment_id)
    buttons.append(button_check)
    buttons = [[button] for button in buttons]
    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard
