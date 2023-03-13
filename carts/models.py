from django.db import models


class Cart(models.Model):
    client = models.OneToOneField(
        'users.User',
        on_delete=models.CASCADE,
        related_name='cart'
    )

    products = models.ManyToManyField(
        'products.Product',
        through='carts.CartProducts',
        related_name='cart'
    )


class CartProducts(models.Model):
    cart = models.ForeignKey(
        'carts.Cart',
        on_delete=models.CASCADE
    )
    products = models.ForeignKey(
        'products.Product',
        on_delete=models.CASCADE
    )
    quantity = models.PositiveSmallIntegerField()
