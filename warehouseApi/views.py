from rest_framework import viewsets

from .serializers import WarehouseSerializer, Warehouse_descriptionSerializer
from .models import Warehouse, Warehouse_description

class WarehouseViewSet(viewsets.ModelViewSet):
    queryset = Warehouse.objects.all().order_by('name')
    serializer_class = WarehouseSerializer

class WarehouseDescriptionViewSet(viewsets.ModelViewSet):
    queryset = Warehouse_description.objects.all().order_by('id')
    serializer_class = Warehouse_descriptionSerializer