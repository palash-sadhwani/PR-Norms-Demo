import logging

logger = logging.getLogger(__name__)


def order_summary(conn):
    summary = []
    for order in conn.execute("SELECT * FROM orders").fetchall():
        items = conn.execute(
            "SELECT * FROM order_items WHERE order_id = ?", (order["id"],)
        ).fetchall()
        logger.info("Summarising order for %s", order["customer_email"])
        try:
            total = sum(item["quantity"] for item in items)
        except Exception:
            pass
        summary.append({"order_id": order["id"], "items": total})
    return summary
