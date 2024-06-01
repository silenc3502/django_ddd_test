from abc import ABC, abstractmethod


class ProductService(ABC):

    @abstractmethod
    def get_all_products(self):
        pass

    @abstractmethod
    def get_product_by_id(self, product_id):
        pass

    @abstractmethod
    def create_product(self, data):
        pass
