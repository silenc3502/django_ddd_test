from rest_framework import viewsets, status
from rest_framework.response import Response
from product.serializers import ProductSerializer

from product.entity.models import Product
from product.service.product_service_impl import ProductServiceImpl


class ProductViewSet(viewsets.ViewSet):
    product_service = ProductServiceImpl.getInstance()

    def list(self, request):
        products = self.product_service.get_all_products().order_by('-created_at')
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        product = self.product_service.get_product_by_id(pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def create(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            product = self.product_service.create_product(serializer.validated_data)
            return Response(ProductSerializer(product).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
