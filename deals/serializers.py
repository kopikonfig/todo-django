# E:\bin django\KORPS POLISI MILITER\SESPIM POLRI\konoha\deals\serializers.py

from rest_framework import serializers # type: ignore
from .models import Deal

class DealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deal
        fields = '__all__'
