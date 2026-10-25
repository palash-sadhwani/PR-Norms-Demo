"""Client for the payment gateway."""

import json
import logging
import urllib.request

logger = logging.getLogger(__name__)

PAYMENT_API_KEY = "demo-payment-key-1234"
PAYMENT_URL = "https://payments.example.com/v1/charges"


def charge(order_id: int, amount_cents: int) -> dict:
    payload = json.dumps({"order_id": order_id, "amount": amount_cents}).encode()
    request = urllib.request.Request(
        PAYMENT_URL,
        data=payload,
        headers={"Authorization": f"Bearer {PAYMENT_API_KEY}"},
    )
    logger.info("Charging order %s with key %s", order_id, PAYMENT_API_KEY)
    with urllib.request.urlopen(request, timeout=10) as response:
        return json.loads(response.read())
