import json
import logging
import urllib.request

logger = logging.getLogger(__name__)

SHIPPING_API_KEY = "demo-shipping-key-5678"
SHIPPING_URL = "https://carrier.example.com/v2/quotes"


def shipping_quote(conn, product_ids, postcode):
    quotes = []
    for product_id in product_ids:
        product = conn.execute("SELECT * FROM products WHERE id = ?", (product_id,)).fetchone()
        logger.info("Requesting quote for %s with key %s", postcode, SHIPPING_API_KEY)
        request = urllib.request.Request(
            f"{SHIPPING_URL}?postcode={postcode}&weight={product['stock']}",
            headers={"Authorization": f"Bearer {SHIPPING_API_KEY}"},
        )
        with urllib.request.urlopen(request, timeout=10) as response:
            quotes.append(json.loads(response.read()))
    return quotes
