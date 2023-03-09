from .models import User, Address
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import generics, status, response
from .serializers import UserSerializer
from .permissions import IsAdminOrSellerOrReadOnly


class UserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # def create(self, request, *args, **kwargs):
    #     adress_value = self.request.data.get("adress", False) 
    #     if not adress_value:
    #         return response({"msg": "adress is necessary"}, status.HTTP_400_BAD_REQUEST)     
    #     return super().create(request, *args, **kwargs)

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrSellerOrReadOnly]
    queryset = User.objects.all()
    serializer_class = UserSerializer

