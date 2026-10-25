import pytest

from inventory.db import connect


@pytest.fixture
def conn():
    connection = connect()
    yield connection
    connection.close()
