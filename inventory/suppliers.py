import csv
import logging

from inventory.config import get_secret

logger = logging.getLogger(__name__)


def supplier_password() -> str:
    return get_secret("SUPPLIER_FTP_PASSWORD")


def parse_quantity(value: str) -> int:
    quantity = int(value)
    if quantity <= 0:
        raise ValueError(f"quantity must be positive, got {quantity}")
    return quantity


def import_stock(conn, path) -> int:
    imported = 0
    with open(path, newline="") as handle:
        for line_number, row in enumerate(csv.DictReader(handle), start=2):
            try:
                quantity = parse_quantity(row["quantity"])
                product_id = int(row["product_id"])
            except (KeyError, ValueError) as exc:
                logger.warning("Skipping CSV line %s: %s", line_number, exc)
                continue
            conn.execute(
                "UPDATE products SET stock = stock + ? WHERE id = ?",
                (quantity, product_id),
            )
            imported += 1
    return imported
