from .views import create_order, order_list, register
from django.urls import path
from . import views

urlpatterns = [
    # path('', create_order, name='create_order'),
    path('orders/', order_list, name='order_list'),  # URL for order list page
    # path('create/', create_order, name='create_order'),
    # path('register/', register, name='register'),
    # path('logout/', register, name='register'),
    path('create/', views.create_order, name='create_order'),

]
