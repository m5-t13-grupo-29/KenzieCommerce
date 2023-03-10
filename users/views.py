from .models import User, Address
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import generics, status, response
from .serializers import UserSerializer
from .permissions import IsAdminOrSellerOrReadOnly


class UserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrSellerOrReadOnly]
    queryset = User.objects.all()
    serializer_class = UserSerializer

