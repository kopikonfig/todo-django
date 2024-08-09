# E:\bin django\KORPS POLISI MILITER\SESPIM POLRI\konoha\leads\serializers.py

from rest_framework import serializers # type: ignore
from .models import Lead

class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = '__all__'
