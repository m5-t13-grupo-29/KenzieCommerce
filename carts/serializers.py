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
        fields = ["id", "products", "cart", "quantity"]

        extra_kwargs = {
            "id": {"read_only": True},
            "cart": {"read_only": True},
            "products": {"read_only": True},
        }

    def create(self, validated_data):

        if validated_data["products"].stock < validated_data["quantity"]:

            raise serializers.ValidationError(
                {"message": "Insufficient stock"}, status.HTTP_400_BAD_REQUEST
            )

        return CartProducts.objects.create(**validated_data)
