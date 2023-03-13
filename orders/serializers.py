from rest_framework import serializers
from .models import Order, OrderProducts
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
        }


class OrderProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderProducts
        fields = [
            "id",
            "price",
            "quantity",
            "product",
        ]

    extra_kwargs = {
        "id": {"read_only": True},
        "price": {"read_only": True},
        "quantity": {"read_only": True},
        "product": {"read_only": True},
    }
