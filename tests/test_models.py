import os
from decimal import Decimal
import pytest
from django.core.exceptions import ValidationError
from wallet.models import Wallet, Transaction

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.development")


@pytest.mark.django_db
class TestWalletModel:
    @pytest.fixture
    def wallet(self):
        return Wallet.objects.create(label="Test Wallet", balance=Decimal("100.0"))

    def test_wallet_str(self, wallet):
        assert str(wallet) == "Test Wallet"

    def test_wallet_balance_default(self):
        new_wallet = Wallet.objects.create(label="New Wallet")
        assert new_wallet.balance == Decimal("0.0")


@pytest.mark.django_db
class TestTransactionModel:
    @pytest.fixture
    def wallet(self):
        return Wallet.objects.create(label="Test Wallet", balance=Decimal("100.0"))

    def test_transaction_str(self, wallet):
        transaction = Transaction.objects.create(wallet=wallet, amount=Decimal("50.0"), txid="tx123")
        assert str(transaction) == "tx123 - 50.0"

    def test_transaction_save(self, wallet):
        transaction_amount = Decimal("50.0")
        Transaction.objects.create(wallet=wallet, amount=transaction_amount)

        wallet.refresh_from_db()
        assert wallet.balance == Decimal("150.0")

    def test_transaction_save_negative_balance(self, wallet):
        transaction = Transaction(wallet=wallet, amount=Decimal("-200.0"))

        with pytest.raises(ValidationError):
            transaction.save()

        wallet.refresh_from_db()
        assert wallet.balance == Decimal("100.0")

    def test_transaction_delete(self, wallet):
        transaction = Transaction.objects.create(wallet=wallet, amount=Decimal("50.0"))
        transaction.delete()

        wallet.refresh_from_db()
        assert wallet.balance == Decimal("100.0")
