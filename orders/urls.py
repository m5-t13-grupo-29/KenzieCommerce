from django.urls import path
from .views import OrderView, OrderDatailView, OrderGetDatailView

urlpatterns = [
    path("orders/", OrderView.as_view()),
    path("orders/<int:order_id>/", OrderDatailView.as_view()),
    path("orders/<int:order_id>/order/", OrderGetDatailView.as_view()),
]
