# E:\bin django\KORPS POLISI MILITER\SESPIM POLRI\konoha\tasks\serializers.py

from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
