"""
URL configuration for order_management project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

# def home_redirect(request):
#     if request.user.is_authenticated:
#         return redirect('create_order')
#     else:
#         return redirect('login')

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', home_redirect, name='home'),
#     path('orders/', include('orders.urls')),
#     path('login/', auth_views.LoginView.as_view(), name='login'),
#     path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
# ]

from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from orders import views as orders_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', auth_views.LoginView.as_view(), name='login'),  # Display login form when user opens the site
    path('register/', orders_views.register, name='register'),
    path('orders/', include('orders.urls')),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]