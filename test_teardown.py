import pytest
from bank import BankAccount


@pytest.fixture
def account():
    print("[setup]")
    acc = BankAccount(100)
    yield acc
    print("[teardown]")


def test_balance_starts_at_100(account):
    assert account.balance == 100


def test_deposit_with_yield_fixture(account):
    account.deposit(10)
    assert account.balance == 110