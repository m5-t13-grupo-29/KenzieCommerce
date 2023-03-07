from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=127)
    category = models.CharField(max_length=127)
    stock = models.IntegerField()
    available = models.BooleanField(default=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    product_image = models.ImageField(null=True, default=None)

    seller = models.ForeignKey(
        'users.User',
        on_delete=models.CASCADE,
        related_name='products'
    )

    def __repr__(self) -> str:
        return f"<Product ({self.id}) - {self.name}>"
