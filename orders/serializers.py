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

    def create(self, validated_data):
        user = get_object_or_404(User, id=validated_data["client_id"])
        list_cart_products = CartProducts.objects.filter(cart_id=user.cart.id).order_by(
            "seller"
        )
        order = Order.objects.create(**validated_data, price=0)
        previous_seller = list_cart_products[0].seller

        for item in list_cart_products:

            product = Product.objects.get(id=item.product_id)

            if product.seller != previous_seller:

                new_order = Order.objects.create(**validated_data, price=0)
                new_order.products.add(
                    product,
                    through_defaults={
                        "quantity": item.quantity,
                        "price": product.price * item.quantity,
                    },
                )
                new_order.price = new_order.price + product.price
                new_order.save()
            else:
                order.products.add(
                    product,
                    through_defaults={
                        "quantity": item.quantity,
                        "price": product.price * item.quantity,
                    },
                )
                order.price = order.price + product.price
                order.save()

            previous_seller = product.seller

        return order


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
