import logging

logger = logging.getLogger(__name__)


def order_summary(conn) -> list[dict]:
    rows = conn.execute(
        """
        SELECT orders.id AS order_id, COALESCE(SUM(order_items.quantity), 0) AS items
        FROM orders LEFT JOIN order_items ON order_items.order_id = orders.id
        GROUP BY orders.id ORDER BY orders.id
        """
    ).fetchall()
    logger.info("Summarised %s orders", len(rows))
    return [dict(row) for row in rows]
