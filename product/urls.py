from django.urls import path, include
from rest_framework.routers import DefaultRouter

from product.controller.views import ProductViewSet

router = DefaultRouter()
router.register(r'product', ProductViewSet, basename='product')

urlpatterns = [
    path('', include(router.urls)),
    path('list/', ProductViewSet.as_view({'get': 'list'}), name='product-list'),
    path('register/', ProductViewSet.as_view({'post': 'create'}), name='product-register'),
    path('read/<int:pk>/', ProductViewSet.as_view({'get': 'retrieve'}), name='product-read'),
]