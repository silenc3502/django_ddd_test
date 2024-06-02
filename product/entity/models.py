from django.db import models

class Product(models.Model):
    productId = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128, null=False)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    # image_name = models.FileField(upload_to='product_images')
    image_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'product'
