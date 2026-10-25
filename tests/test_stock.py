import pytest

from inventory.products import add_product, get_product
from inventory.stock import reserve_items


def test_reservation_never_makes_stock_negative(conn):
    product_id = add_product(conn, "Widget", 2, 100)
    with pytest.raises(ValueError):
        reserve_items(conn, [(product_id, 3)])
    assert get_product(conn, product_id)["stock"] == 2


def test_reservation_rejects_non_positive_quantity(conn):
    product_id = add_product(conn, "Widget", 2, 100)
    with pytest.raises(ValueError):
        reserve_items(conn, [(product_id, -1)])
