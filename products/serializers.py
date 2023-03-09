from rest_framework import serializers
from .models import Product, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            "id",
            "name",

        ]

        # extra_kwargs = {
        #     "products": {"read_only": True}
        # }


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
    
    categories = CategorySerializer(many=True)

    class Meta:
        model = Product
        fields = [
            "id",
            "name",
            "categories",
            "stock",
            "price",
            "product_image",
            "seller"
        ]

        extra_kwargs = {
            "seller": {"read_only": True},
            "product_image": {"read_only": True}
        }
