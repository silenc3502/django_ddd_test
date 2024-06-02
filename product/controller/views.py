import os

from rest_framework import viewsets, status
from rest_framework.response import Response

from django_ddd_test import settings
from product.serializers import ProductSerializer

from product.entity.models import Product
from product.service.product_service_impl import ProductServiceImpl


class ProductViewSet(viewsets.ViewSet):
    product_service = ProductServiceImpl.getInstance()

    def list(self, request):
        products = self.product_service.get_all_products().order_by('-created_at')
        print('products:', products)
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        product = self.product_service.get_product_by_id(pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def create(self, request):
        try:
            data = request.data
            image_file = request.FILES.get('image')
            product_name = data.get('name')
            product_description = data.get('description')
            product_price = data.get('price')

            print(f'Received data: {data}')
            print(f'Image file: {image_file}')
            print(f'Product name: {product_name}')
            print(f'Product description: {product_description}')
            print(f'Product price: {product_price}')

            if not all([product_name, product_description, product_price, image_file]):
                return Response({'error': '모든 필드를 채워주세요.'}, status=status.HTTP_400_BAD_REQUEST)

            # 이미지 파일 저장 경로 설정
            upload_dir = os.path.join(settings.BASE_DIR, '../vuetify-board-with-django/src/assets/uploadImgs')
            if not os.path.exists(upload_dir):
                os.makedirs(upload_dir)

            image_path = os.path.join(upload_dir, image_file.name)
            with open(image_path, 'wb+') as destination:
                for chunk in image_file.chunks():
                    destination.write(chunk)

            # 여기서 Product 객체를 생성하고 데이터베이스에 저장합니다.
            product = Product(
                name=product_name,
                description=product_description,
                price=product_price,
                image_name=image_file.name  # image 대신 image_name 사용
            )
            product.save()

            print(f'Product created: {product}')

            return Response({'message': '상품이 등록되었습니다.'}, status=status.HTTP_201_CREATED)

        except Exception as e:
            print('Error occurred during product creation:', e)
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

