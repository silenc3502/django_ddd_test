from product.entity.models import Product
from product.repository.product_repository import ProductRepository


class ProductRepositoryImpl(ProductRepository):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()
        return cls.__instance

    def get_all_products(self):
        return Product.objects.all()

    def get_product_by_id(self, product_id):
        try:
            return Product.objects.get(productId=product_id)
        except Product.DoesNotExist:
            return None

    def create_product(self, data):
        return Product.objects.create(**data)
