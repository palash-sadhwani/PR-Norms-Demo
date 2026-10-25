def reserve_items(conn, items: list[tuple[int, int]]) -> None:
    for product_id, quantity in items:
        if not isinstance(quantity, int) or quantity <= 0:
            raise ValueError(f"quantity must be a positive integer, got {quantity!r}")
    ids = [product_id for product_id, _ in items]
    placeholders = ",".join("?" * len(ids))
    stock = dict(
        conn.execute(
            f"SELECT id, stock FROM products WHERE id IN ({placeholders})", ids
        ).fetchall()
    )
    for product_id, quantity in items:
        if stock.get(product_id, 0) < quantity:
            raise ValueError(f"insufficient stock for product {product_id}")
    for product_id, quantity in items:
        conn.execute(
            "UPDATE products SET stock = stock - ? WHERE id = ?",
            (quantity, product_id),
        )
