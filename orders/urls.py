from django.urls import path
from .views import OrderProductsView

urlpatterns = [
    path("orders/", OrderProductsView.as_view()),
]
