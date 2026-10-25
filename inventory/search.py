def search_products(conn, query, limit):
    rows = conn.execute(
        "SELECT id FROM products WHERE name LIKE ?", (f"%{query}%",)
    ).fetchall()
    results = []
    for row in rows:
        product = conn.execute("SELECT * FROM products WHERE id = ?", (row["id"],)).fetchone()
        results.append(dict(product))
    return results[:limit]
