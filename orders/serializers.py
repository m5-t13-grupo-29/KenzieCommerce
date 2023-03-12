from rest_framework import serializers
from .models import Order
from carts.models import Cart, CartProducts
from rest_framework.views import status
from django.shortcuts import get_object_or_404
from users.models import User
from products.models import Product


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = [
            "id",
            "price",
            "status",
            "created_at",
            "client",
            "products",
        ]

        extra_kwargs = {
            "id": {"read_only": True},
            "created_at": {"read_only": True},
            "client": {"read_only": True},
            "products": {"read_only": True},
            "price": {"read_only": True},
            "status": {"read_only": True},
        }

    def create(self, validated_data):
        user = get_object_or_404(User, id=validated_data["client_id"])
        list_cart_products = CartProducts.objects.filter(cart_id=user.cart.id)
        order = Order.objects.create(**validated_data, price=0)
        for item in list_cart_products:
            cart_product = get_object_or_404(CartProducts, id=item.id)
            product = get_object_or_404(Product, id=cart_product.products_id)

            print("product", product.name, "product stock", product.stock)
            print("product seller", product.seller_id)
            print("quantidade", cart_product.quantity)

            order.products.add(product, quantity=item.quantity)

        order.save()
        import ipdb

        ipdb.set_trace()

        return cart_product
