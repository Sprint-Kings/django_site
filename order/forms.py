from django import forms
from .models import Order


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['fullname', 'address',
                  'card_number', 'cvv', 'expiration']