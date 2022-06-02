from ajax_select.fields import AutoCompleteSelectMultipleField, AutoCompleteField
from .models import Shipping
from django import forms


class ShippingForm(forms.ModelForm):
    supplier = AutoCompleteField("supplier")

    class Meta:
        model = Shipping
