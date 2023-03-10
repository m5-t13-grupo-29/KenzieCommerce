from django.urls import path
from .views import CartProductsView, CartProductsDetailView

urlpatterns = [
    path("carts/<int:pk>/", CartProductsView.as_view()),
    path("carts/product/<int:products_id>/", CartProductsDetailView.as_view()),
]
