from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=127)
    stock = models.IntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    product_image = models.ImageField(null=True, default=None)

    seller = models.ForeignKey(
        'users.User',
        on_delete=models.CASCADE,
        related_name='products'
    )

    def __repr__(self) -> str:
        return f"<Product ({self.id}) - {self.name}>"


class Category(models.Model):
    name = models.CharField(max_length=80)

    products = models.ManyToManyField(
        'products.Product',
        related_name='categories'
    )
