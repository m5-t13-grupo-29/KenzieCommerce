from rest_framework import serializers
from .models import Cart, CartProducts
from rest_framework.views import status


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = [
            "id",
            "client",
            "products",
        ]

        extra_kwargs = {
            "id": {"read_only": True},
            "client": {"read_only": True},
        }


class CartProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartProducts
        fields = ["id", "product", "cart", "quantity", "seller"]

        extra_kwargs = {
            "id": {"read_only": True},
            "cart": {"read_only": True},
            "product": {"read_only": True},
            "seller": {"read_only": True},
        }

    def create(self, validated_data):

        if not CartProducts.objects.filter(
            cart_id=validated_data["cart"].id, product_id=validated_data["product"].id
        ).exists():

            if validated_data["product"].stock < validated_data["quantity"]:
                raise serializers.ValidationError(
                    {"message": "Insufficient stock"}, status.HTTP_400_BAD_REQUEST
                )
            return CartProducts.objects.create(**validated_data)

        else:
            product_cart = CartProducts.objects.get(
                cart_id=validated_data["cart"].id,
                product_id=validated_data["product"].id,
            )

            quantity_product = product_cart.quantity + validated_data["quantity"]

            if quantity_product > validated_data["product"].stock:
                raise serializers.ValidationError(
                    {"message": "Insufficient stock"}, status.HTTP_400_BAD_REQUEST
                )
            else:
                product_cart.quantity = quantity_product
                product_cart.save()
                return product_cart
