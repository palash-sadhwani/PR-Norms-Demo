def add_product(conn, name: str, stock: int, price_cents: int) -> int:
    cursor = conn.execute(
        "INSERT INTO products (name, stock, price_cents) VALUES (?, ?, ?)",
        (name, stock, price_cents),
    )
    return cursor.lastrowid


def get_product(conn, product_id: int) -> dict | None:
    row = conn.execute("SELECT * FROM products WHERE id = ?", (product_id,)).fetchone()
    return dict(row) if row else None
