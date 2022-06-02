from ajax_select.fields import AutoCompleteSelectMultipleField, AutoCompleteField
from .models import Shipping
from django import forms


class ShippingForm(forms.ModelForm):
    supplier = AutoCompleteField("suppliers")
    supplier.label = "Поставщик"

    class Meta:
        model = Shipping
        fields = (
            "date",
            "supplier",
            "factory",
            "order",
            "seller",
            "buyer",
            "waybill",
            "sales_tax",
            "product",
            "quantity",
            "purchase_price",
            "sales_price",
            "delivery_price",
            "driver",
            "address",
            "dispatcher",
            "comment",
        )
