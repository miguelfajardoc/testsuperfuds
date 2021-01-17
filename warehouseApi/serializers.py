from rest_framework import serializers
from .models import Warehouse, Warehouse_description
from django import utils

class Warehouse_descriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warehouse_description
        fields = ('id', 'phone', 'city', 'address', 'created_at', 'updated_at', 'warehouse_id')
    


class WarehouseSerializer(serializers.ModelSerializer):
    description = Warehouse_descriptionSerializer(many=True)
    class Meta:
        model = Warehouse
        fields = ('id', 'name', 'headquartersNumber', 'created_at', 'updated_at', 'description')

    def create(self, data):
        descriptions = data.pop('description')

        warehouse = Warehouse.objects.create(**data)

        for description in descriptions:
            new_desc = Warehouse_description.objects.create(**description)
            new_desc.warehouse_id = warehouse
            new_desc.save()
        warehouse.save()
        return warehouse
