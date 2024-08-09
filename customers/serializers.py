# E:\bin django\KORPS POLISI MILITER\SESPIM POLRI\konoha\customers\serializers.py

from rest_framework import serializers # type: ignore
from .models import Customer

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'
