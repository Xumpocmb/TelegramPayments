from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
import yookassa_payment
from keyboards.payment_keyboard import make_payment_keyboard

router: Router = Router()


@router.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer(f'Hello, {message.from_user.username}!')


@router.message(Command("pay"))
async def cmd_pay(message: Message):
    payment_link, payment_id = yookassa_payment.create_payment()
    await message.answer(f'{message.from_user.username}, its link for payment: {payment_link}, payment id: {payment_id}',
                         reply_markup=make_payment_keyboard(payment_link, payment_id))


@router.callback_query()
async def check_payment(callback):
    payment_id = callback.data
    if yookassa_payment.check_payment(payment_id):
        await callback.message.answer('Payment succeeded!')
        await callback.answer()
    else:
        await callback.message.answer('Payment failed!')
        await callback.answer()
