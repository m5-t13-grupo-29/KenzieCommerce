from rest_framework import permissions
from rest_framework.views import Request, View

class IsAdminOrSellerOrReadOnly(permissions.BasePermission):
    def has_permission(self, request: Request, view: View):
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return (
            request.user.is_authenticated 
            and request.user.is_superuser
            or request.user.is_seller
        )