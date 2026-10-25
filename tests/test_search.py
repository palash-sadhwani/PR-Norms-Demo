import pytest

from inventory.products import add_product
from inventory.search import search_products


def test_search_respects_limit(conn):
    for name in ("Red widget", "Blue widget", "Green widget"):
        add_product(conn, name, 1, 100)
    assert [p["name"] for p in search_products(conn, "widget", 2)] == [
        "Red widget",
        "Blue widget",
    ]


@pytest.mark.parametrize("query,limit", [("", 5), ("widget", 0), ("widget", 500)])
def test_search_rejects_invalid_input(conn, query, limit):
    with pytest.raises(ValueError):
        search_products(conn, query, limit)
