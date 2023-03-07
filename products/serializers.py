from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        return Product.objects.create(**validated_data)

    class Meta:
        model = Product
        fields = [
            "id",
            "name",
            "category",
            "stock",
            "available",
            "price",
            "product_image",
            "seller"
        ]

        extra_kwargs = {
            "seller": {"read_only": True},
            "product_image": {"read__only": True}
        }
