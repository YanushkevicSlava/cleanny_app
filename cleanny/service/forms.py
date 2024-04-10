from django import forms
from .models import Order


class FormCreateOrder(forms.ModelForm):
    """Форма создания заказа"""
    class Meta:
        model = Order
        fields = '__all__'
        widgets = {
            'cleaning_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            # 'services': forms.SelectMultiple()
        }
