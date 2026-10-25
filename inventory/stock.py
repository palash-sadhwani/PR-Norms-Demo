def reserve_items(conn, items):
    for product_id, quantity in items:
        product = conn.execute(
            "SELECT stock FROM products WHERE id = ?", (product_id,)
        ).fetchone()
        if product["stock"] >= quantity:
            conn.execute(
                "UPDATE products SET stock = stock - ? WHERE id = ?",
                (quantity, product_id),
            )
