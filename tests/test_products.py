from inventory.products import add_product, get_product


def test_add_and_get_product(conn):
    product_id = add_product(conn, "Widget", 5, 250)
    assert get_product(conn, product_id)["stock"] == 5
