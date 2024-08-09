# E:\bin django\KORPS POLISI MILITER\SESPIM POLRI\konoha\notifications\serializers.py

from rest_framework import serializers # type: ignore
from .models import Notification

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'
