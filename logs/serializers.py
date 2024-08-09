# E:\bin django\KORPS POLISI MILITER\SESPIM POLRI\konoha\logs\serializers.py

from rest_framework import serializers # type: ignore
from .models import LogEntry

class LogEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = LogEntry
        fields = '__all__'
