from django import forms
from django.forms import widgets

from webapp.models import CATEGORY_CHOICES


class ElShopForm(forms.Form):
    name = forms.CharField(max_length=100, required=True, label="Наименование товара")
    cost = forms.DecimalField(max_digits=7, decimal_places=2, required=True, label="Стоимость")
    remnant = forms.IntegerField(min_value=0, required=True, label="Остаток")
    category = forms.ChoiceField(choices=CATEGORY_CHOICES)
