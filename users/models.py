from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    image = models.CharField(max_length=127, blank=True)
    email = models.EmailField(
        max_length=127,
        unique=True,
        error_messages={
            "unique": "A user with that email already exists.",
        }
    )
    is_seller = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"<User [{self.id}] - {self.first_name}>"


class Address(models.Model):
    street = models.CharField(max_length=127)
    number = models.IntegerField()
    city = models.CharField(max_length=127)
    state = models.CharField(max_length=2)
    zip_code = models.CharField(max_length=8)
    country = models.CharField(max_length=127)

    user = models.OneToOneField(
        'users.User',
        on_delete=models.CASCADE,
        related_name='address'
    )

    def __repr__(self) -> str:
        return f"<Address ({self.id}) - {self.street}>"
