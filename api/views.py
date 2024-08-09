# E:\bin django\KORPS POLISI MILITER\SESPIM POLRI\konoha\api\views.py

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import SomeModel
from .serializers import SomeModelSerializer

class SomeModelListView(generics.ListCreateAPIView):
    queryset = SomeModel.objects.all()
    serializer_class = SomeModelSerializer
    permission_classes = [IsAuthenticated]  # Menambahkan permission

class SomeModelDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SomeModel.objects.all()
    serializer_class = SomeModelSerializer
    permission_classes = [IsAuthenticated]  # Menambahkan permission
