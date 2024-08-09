# E:\bin django\KORPS POLISI MILITER\SESPIM POLRI\konoha\emails\serializers.py

from rest_framework import serializers # type: ignore
from .models import EmailTemplate, EmailIntegration

class EmailTemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailTemplate
        fields = '__all__'

class EmailIntegrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailIntegration
        fields = '__all__'
