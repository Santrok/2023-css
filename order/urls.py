from django.urls import path

from order.views import order_create

urlpatterns = [
    path('order_create/', order_create, name='order_create')
]