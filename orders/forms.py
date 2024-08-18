from django import forms
from .models import Order

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, ButtonHolder, Submit

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = [
            'name', 'email', 'phone', 'selected_items',
            'delivery_option', 'delivery_address', 'pickup_date',
            'pickup_time', 'payment_option', 'card_number',
            'expiry_date', 'cvv', 'instructions'
        ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'selected_items': forms.Textarea(attrs={'class': 'form-control'}),
            'delivery_option': forms.Select(attrs={'class': 'form-select'}),
            'delivery_address': forms.TextInput(attrs={'class': 'form-control'}),
            'pickup_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'pickup_time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'payment_option': forms.Select(attrs={'class': 'form-select'}),
            'card_number': forms.TextInput(attrs={'class': 'form-control'}),
            'expiry_date': forms.TextInput(attrs={'class': 'form-control'}),
            'cvv': forms.TextInput(attrs={'class': 'form-control'}),
            'instructions': forms.Textarea(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'name',
            'email',
            'phone',
            'selected_items',
            'delivery_option',
            'delivery_address',
            'pickup_date',
            'pickup_time',
            'payment_option',
            'card_number',
            'expiry_date',
            'cvv',
            'instructions',
            ButtonHolder(
                Submit('submit', 'Submit Order', css_class='btn btn-primary')
            )
        )

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
