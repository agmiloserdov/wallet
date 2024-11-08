import uuid
from decimal import Decimal

from django.core.exceptions import ValidationError
from django.db import models, transaction
from django.utils.translation import gettext_lazy as _


class Wallet(models.Model):
    label = models.CharField(verbose_name=_("Label"), max_length=255)
    balance = models.DecimalField(verbose_name=_("Balance"), max_digits=28, decimal_places=18, default=Decimal("0.0"))

    def __str__(self):
        return self.label


class Transaction(models.Model):
    wallet = models.ForeignKey(
        verbose_name=_("Wallet"), to=Wallet, on_delete=models.CASCADE, related_name="transactions"
    )
    txid = models.CharField(
        verbose_name=_("Transaction id"), max_length=255, unique=True, default=uuid.uuid4, editable=False, db_index=True
    )
    created_at = models.DateTimeField(verbose_name=_("Created At"), auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name=_("Updated at"), auto_now=True)
    amount = models.DecimalField(verbose_name=_("Amount"), max_digits=28, decimal_places=18)

    @transaction.atomic
    def save(self, *args, **kwargs) -> None:  # noqa
        new_balance = self.wallet.balance + self.amount
        if new_balance < 0:
            raise ValidationError("Wallet balance cannot be negative.")
        super().save(*args, **kwargs)

        self.wallet.balance = new_balance
        self.wallet.save(update_fields=["balance"])

    def delete(self, *args, **kwargs) -> None:
        self.wallet.balance -= self.amount
        if self.wallet.balance < 0:
            raise ValidationError("Wallet balance cannot be negative after deleting this transaction.")
        super().delete(*args, **kwargs)
        self.wallet.save(update_fields=["balance"])

    def __str__(self):
        return f"{self.txid} - {self.amount}"
