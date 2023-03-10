from rest_framework import serializers
from .models import User, Address


class AddressSerializer(serializers.ModelSerializer):
    def update(self, instance: Address, validated_data: dict) -> Address:
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance

    class Meta:
        model = Address
        fields = [
            "id",
            "zip_code",
            "country",
            "state",
            "city",
            "street",
            "number",
        ]

        extra_kwargs = {
            "id": {"read_only": True}
        }

class UserSerializer(serializers.ModelSerializer):
    address = AddressSerializer()
    def create(self, validated_data: dict) -> User:
        adress_data = validated_data.pop("address")
        address_object = Address.objects.create(**adress_data)

        if validated_data["is_superuser"]:
            return User.objects.create_superuser(**validated_data, address=address_object)
        
        return User.objects.create_user(**validated_data, address=address_object)
    
    def update(self, instance: User, validated_data: dict) -> User:
        for key, value in validated_data.items():
            if key == "password":
                instance.set_password(value)
            else:
                setattr(instance, key, value)

        instance.save()
        return instance

    class Meta:
        model = User
        fields = [
            "id",
            "first_name",
            "last_name", 
            "image",
            "email",                    
            "is_seller",
            "is_superuser",
            "password",
            "username",
            "address",
        ]

        extra_kwargs = {
            "id": {"read_only": True},
            "password": {"write_only": True},
        }


class SellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "first_name",
            "last_name",
            "email"
        ]