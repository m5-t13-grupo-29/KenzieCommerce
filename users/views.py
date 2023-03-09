from .models import User
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import generics
from .serializers import UserSerializer
from .permissions import IsAdminOrSellerOrReadOnly, IsAdminToList


class UserView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminToList]

    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrSellerOrReadOnly]
    queryset = User.objects.all()
    serializer_class = UserSerializer

