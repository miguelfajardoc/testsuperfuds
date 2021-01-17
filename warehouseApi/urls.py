from django.urls import include, path
from rest_framework import routers
from .views import WarehouseViewSet, WarehouseDescriptionViewSet

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'warehouse', WarehouseViewSet, basename='Warehouse')
router.register(r'warehouse_description', WarehouseDescriptionViewSet, basename='Warehouse_description')

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]