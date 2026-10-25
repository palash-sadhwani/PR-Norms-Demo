import pytest

from inventory.payments import build_charge_request


def test_charge_request_reads_key_from_environment(monkeypatch):
    monkeypatch.setenv("PAYMENT_API_KEY", "test-key")
    request = build_charge_request(7, 500)
    assert request.get_header("Authorization") == "Bearer test-key"


def test_charge_request_requires_key(monkeypatch):
    monkeypatch.delenv("PAYMENT_API_KEY", raising=False)
    with pytest.raises(RuntimeError):
        build_charge_request(7, 500)
