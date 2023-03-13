from rest_framework import permissions
from rest_framework.views import Request, View
from .models import Order, OrderProducts


class IsProductSeller(permissions.BasePermission):
    def has_object_permission(self, request: Request, view: View, obj: Order):
        order_product = OrderProducts.objects.filter(order_id=obj.id).first()

        if request.user.is_authenticated and request.user.is_superuser:
            return True

        return (
            request.user.is_authenticated
            and request.user.id == order_product.product.seller.id
        )


class IsAdminOrSeller(permissions.BasePermission):
    def has_permission(self, request: Request, view: View):

        if request.user.is_superuser or request.user.is_seller:
            return True

        return False


class IsAdminOrSellerOrOwner(permissions.BasePermission):
    def has_object_permission(self, request: Request, view: View, obj: Order):

        if (
            request.user.is_authenticated
            and request.user.is_superuser
            or request.user.is_seller
        ):
            return True

        return request.user.is_authenticated and request.user.id == obj.client_id
