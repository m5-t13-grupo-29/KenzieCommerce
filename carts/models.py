from django.db import models


class Cart(models.Model):
    client = models.OneToOneField(
        'users.User',
        on_delete=models.CASCADE,
        related_name='cart'
    )

    products = models.ManyToManyField(
        'products.Product',
        related_name='products'
    )
