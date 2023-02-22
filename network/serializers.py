from rest_framework import serializers

from network.models import Company


class CompanySerializer(serializers.ModelSerializer):
    """Вывод Компаний, с запретом изменения значения задолженности перед поставщиком"""
    product = serializers.StringRelatedField(many=True, read_only=True)
    debt = serializers.DecimalField(max_digits=12, decimal_places=2, read_only=True)

    class Meta:
        model = Company
        fields = ('id', 'title', 'country', 'vendor', 'debt', 'product')
        read_only_fields = ('debt')