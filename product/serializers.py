from rest_framework import serializers
from .entity.models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['productId', 'name', 'description', 'price', 'image_name', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']