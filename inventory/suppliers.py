import csv

SUPPLIER_FTP_PASSWORD = "supplier-pass-2024"


def import_stock(conn, path):
    with open(path, newline="") as handle:
        for row in csv.DictReader(handle):
            try:
                quantity = int(row["quantity"])
                conn.execute(
                    "UPDATE products SET stock = stock + ? WHERE id = ?",
                    (quantity, int(row["product_id"])),
                )
            except:
                pass
