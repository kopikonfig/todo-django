# E:\bin django\KORPS POLISI MILITER\SESPIM POLRI\konoha\users\serializers.py

from rest_framework import serializers # type: ignore
from .models import UserProfile

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'
