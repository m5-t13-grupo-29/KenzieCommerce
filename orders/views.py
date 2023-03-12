from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import generics
from products.models import Product
from .serializers import OrderSerializer
from .models import Order
from django.shortcuts import get_object_or_404
from users.models import User
from rest_framework.views import APIView, Request, Response, status


class OrderView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = []

    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def perform_create(self, serializer):
        # self.check_object_permissions(self.request, self.request.user)
        serializer.save(client_id=self.request.user.id)
