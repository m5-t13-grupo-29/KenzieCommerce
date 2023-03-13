from rest_framework import permissions
from rest_framework.views import Request, View
from .models import User


class IsAdminOrSellerOrReadOnly(permissions.BasePermission):
    def has_permission(self, request: Request, view: View):
        if request.method in permissions.SAFE_METHODS:
            return True

        return (
            request.user.is_authenticated
            and (request.user.is_superuser
            or request.user.is_seller)
        )


class IsAdminToList(permissions.BasePermission):
    def has_permission(self, request: Request, view: View):
        if (request.method in permissions.SAFE_METHODS):
            return (request.user.is_authenticated
                    and request.user.is_superuser)

        return True


class IsAdminOrAccountOwner(permissions.BasePermission):
    def has_object_permission(self, request: Request, view: View, obj: User):
        if request.user.is_authenticated and request.user.is_superuser:
            return True

        return (request.user.is_authenticated and
                request.user.id == obj.id)
