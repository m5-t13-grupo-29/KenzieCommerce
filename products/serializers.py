from rest_framework import serializers
from .models import Product, Category
from users.serializers import SellerSerializer


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            "id",
            "name",
        ]


class ProductSerializer(serializers.ModelSerializer):
    def create(self, validated_data: dict) -> Product:
        categories_data = validated_data.pop("categories")
        product = Product.objects.create(**validated_data)

        for category in categories_data:
            categoryExists = Category.objects.filter(
                name__iexact=category["name"]
            ).first()

            if not categoryExists:
                categoryExists = Category.objects.create(**category)

            product.categories.add(categoryExists)

        return product

    def update(self, instance: Product, validated_data: dict) -> Product:
        if "categories" in validated_data:
            categories_data = validated_data.pop("categories")

            for category in categories_data:
                categoryExists = Category.objects.filter(
                    name__iexact=category["name"]
                ).first()

                if not categoryExists:
                    categoryExists = Category.objects.create(**category)

                instance.categories.add(categoryExists)

        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save()
        return instance

    categories = CategorySerializer(many=True)
    seller = SellerSerializer(read_only=True)

    class Meta:
        model = Product
        fields = [
            "id",
            "name",
            "stock",
            "price",
            "product_image",
            "categories",
            "seller"
        ]

        extra_kwargs = {
            "product_image": {"read_only": True}
        }
