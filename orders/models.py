from django.db import models


class StatusOrder(models.TextChoices):
    PEDIDO_REALIZADO = 'Pedido realizado'
    EM_ANDAMENTO = 'Pedido em andamento'
    ENTREGUE = 'Pedido entregue'


class Order(models.Model):
    price = models.DecimalField(max_digits=8, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=20,
        choices=StatusOrder.choices,
        default=StatusOrder.PEDIDO_REALIZADO
    )

    client = models.ForeignKey(
        'users.User',
        on_delete=models.CASCADE,
        related_name='orders'
    )
    products = models.ManyToManyField(
        'products.Product',
        related_name='orders'
    )
