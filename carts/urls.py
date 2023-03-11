from django.urls import path
from .views import CartView, CartProductsView, CartProductsDetailView

urlpatterns = [
    path("carts/", CartView.as_view()),
    path("carts/<int:pk>/", CartProductsView.as_view()),
    path("carts/product/<int:products_id>/", CartProductsDetailView.as_view()),
]
