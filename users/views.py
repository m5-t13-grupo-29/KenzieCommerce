from .models import User, Address
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import generics, serializers, status
from .serializers import UserSerializer, AddressSerializer
from .permissions import IsAdminOrAccountOwner, IsAdminToList


class UserView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminToList]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrAccountOwner]
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_update(self, serializer):
        if not self.request.user.is_superuser:
            if "is_seller" in serializer.validated_data:
                return serializers.ValidationError({"message": "Unauthorized"}, status.HTTP_401_UNAUTHORIZED)
        serializer.save()


class AdressDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrAccountOwner]
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
