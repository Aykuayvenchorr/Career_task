from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import (
    generics,
    permissions
)

from network import serializers
from network.models import Company
from network.permissions import IsActiveUsers


class CompanyView(generics.ListAPIView):
    """
    Вьюшка списка контрагентов торговой сети
    """
    queryset = Company.objects.all()
    serializer_class = serializers.CompanySerializer
    permission_classes = [permissions.IsAuthenticated, IsActiveUsers]
    filter_backends = [DjangoFilterBackend, ]
    filterset_fields = ['country']