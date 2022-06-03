from ajax_select.fields import AutoCompleteField
from django import forms

from .models import Shipping


class ShippingForm(forms.ModelForm):
    supplier = AutoCompleteField(
        "supplier", label="Поставщик", required=False, help_text=None
    )
    factory = AutoCompleteField(
        "factory", label="Завод", required=False, help_text=None
    )
    order = AutoCompleteField("order", label="Приказ", required=False, help_text=None)
    seller = AutoCompleteField(
        "seller", label="Продавец", required=False, help_text=None
    )
    buyer = AutoCompleteField(
        "buyer", label="Покупатель", required=False, help_text=None
    )
    product = AutoCompleteField(
        "product", label="Продукция", required=False, help_text=None
    )
    driver = AutoCompleteField(
        "driver", label="Водитель", required=False, help_text=None
    )
    address = AutoCompleteField(
        "address", label="Адрес", required=False, help_text=None
    )

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
