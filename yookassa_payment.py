import os
import uuid

from dotenv import load_dotenv
from yookassa import Configuration
from yookassa import Payment

load_dotenv()

Configuration.account_id = os.getenv('shopId')
Configuration.secret_key = os.getenv('YooKassa_API')
idempotence_key = str(uuid.uuid4())


def create_payment():
    payment = Payment.create(
        {
            "amount": {
                "value": "112.00",
                "currency": "RUB"
            },
            "payment_method_data": {
                "type": "bank_card"
            },
            "confirmation": {
                "type": "redirect",
                "return_url": "https://t.me/xumpocmb_test_bot"
            },
            "capture": True,
            "description": "Заказ №0"
        }, idempotence_key
    )

    url = payment.confirmation.confirmation_url
    return url, payment.id


def check_payment(payment_id):
    payment = Payment.find_one(payment_id)
    if payment.status == 'succeeded':
        return True
    else:
        return False
