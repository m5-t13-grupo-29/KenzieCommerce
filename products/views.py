from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import Product
from .serializers import ProductSerializer
from .permissions import IsAdminOrProductSeller
from users.permissions import IsAdminOrSellerOrReadOnly


class ProductView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrSellerOrReadOnly]

    queryset = Product.objects.all().order_by("id")
    serializer_class = ProductSerializer

    def get_queryset(self):
        name_params = self.request.query_params.get("name")
        category_params = self.request.query_params.get("category")

        if name_params:
            queryset = Product.objects.filter(name__icontains=name_params)
            return queryset
        
        if category_params:
            queryset = Product.objects.filter(categories__name__icontains=category_params)
            return queryset
        
        return super().get_queryset()

    def perform_create(self, serializer):
        serializer.save(seller=self.request.user)


class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrProductSeller]

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    lookup_url_kwarg = "product_id"