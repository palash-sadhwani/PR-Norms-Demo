MAX_LIMIT = 100


def search_products(conn, query: str, limit: int) -> list[dict]:
    if not isinstance(query, str) or not query.strip():
        raise ValueError("query must be a non-empty string")
    if not isinstance(limit, int) or not 0 < limit <= MAX_LIMIT:
        raise ValueError(f"limit must be between 1 and {MAX_LIMIT}")
    rows = conn.execute(
        "SELECT * FROM products WHERE name LIKE ? ORDER BY id LIMIT ?",
        (f"%{query.strip()}%", limit),
    ).fetchall()
    return [dict(row) for row in rows]
