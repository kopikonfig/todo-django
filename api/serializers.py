# E:\bin django\KORPS POLISI MILITER\SESPIM POLRI\konoha\api\serializers.py

from rest_framework import serializers # type: ignore
from .models import SomeModel

class SomeModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = SomeModel
        fields = '__all__'
