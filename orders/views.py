from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import generics
from products.models import Product
from .serializers import OrderSerializer
from .models import Order
from django.shortcuts import get_object_or_404
from users.models import User
from carts.models import Cart, CartProducts


class OrderProductsView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = []

    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def perform_create(self, serializer):
        user = get_object_or_404(User, id=self.request.user.id)
        list_cart_products = CartProducts.objects.filter(cart_id=user.cart.id)
        for item in list_cart_products:
            cart_product = get_object_or_404(CartProducts, id=item.id)
            product = get_object_or_404(Product, id=cart_product.products_id)
            serializer.save(price=item.price, quantity=item.quantity, product=product)
