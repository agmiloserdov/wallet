from django_filters.rest_framework.backends import DjangoFilterBackend
from rest_framework import viewsets, filters, permissions

from wallet.api.pagination import StandardResultsSetPagination
from wallet.api.serializers import WalletSerializer, TransactionSerializer
from wallet.models import Wallet, Transaction


class WalletViewSet(viewsets.ModelViewSet):
    queryset = Wallet.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = WalletSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ["label", "balance"]
    ordering = ["label"]


class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all().order_by("-id")
    permission_classes = (permissions.AllowAny,)
    serializer_class = TransactionSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ["wallet_id"]
    ordering_fields = ["amount", "txid"]
    ordering = ["-id"]

    def perform_create(self, serializer):
        serializer.save()
