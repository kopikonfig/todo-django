# E:\bin django\KORPS POLISI MILITER\SESPIM POLRI\konoha\reports\serializers.py

from rest_framework import serializers
from .models import Report

class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = '__all__'
