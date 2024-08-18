from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Order
from .forms import OrderForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('create_order')  # Redirect to order form after successful registration
    else:
        form = UserCreationForm()
    return render(request, 'orders/register.html', {'form': form})


@login_required
def create_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            if order.delivery_option == 'pickup':
                order.delivery_address = None
            if order.payment_option != 'card':
                order.card_number = None
                order.expiry_date = None
                order.cvv = None
            order.save()
            return redirect('order_list')  # Redirect to order list page
    else:
        form = OrderForm()
    return render(request, 'orders/create_order.html', {'form': form})

@login_required
def order_list(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'orders/order_list.html', {'orders': orders})

