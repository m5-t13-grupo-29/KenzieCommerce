from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import User, Address


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = "__all__"

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    address = AddressSerializer()
    def create(self, validated_data: dict) -> User:
        adress_data = validated_data.pop("address")
        address_object = Address.objects.create(**adress_data)
        return User.objects.create_superuser(**validated_data, address = address_object)
    
    def update(self, instance: User, validated_data: dict) -> User:
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.set_password(validated_data["password"])
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
                    "password",
                    "username",
                    "address",
        ]
