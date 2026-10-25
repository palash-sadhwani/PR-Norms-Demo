"""Client for the payment gateway."""

import json
import logging
import urllib.request

from inventory.config import get_secret

logger = logging.getLogger(__name__)

PAYMENT_URL = "https://payments.example.com/v1/charges"


def build_charge_request(order_id: int, amount_cents: int) -> urllib.request.Request:
    payload = json.dumps({"order_id": order_id, "amount": amount_cents}).encode()
    return urllib.request.Request(
        PAYMENT_URL,
        data=payload,
        headers={"Authorization": f"Bearer {get_secret('PAYMENT_API_KEY')}"},
    )


def charge(order_id: int, amount_cents: int) -> dict:
    request = build_charge_request(order_id, amount_cents)
    logger.info("Charging order %s", order_id)
    with urllib.request.urlopen(request, timeout=10) as response:
        return json.loads(response.read())
