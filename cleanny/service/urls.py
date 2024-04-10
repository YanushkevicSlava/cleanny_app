from django.urls import path
from .views import calculate_cost, order_create

urlpatterns = [
    path('', calculate_cost, name='index'),
    path("orders-create/", order_create, name="order_create"),
]