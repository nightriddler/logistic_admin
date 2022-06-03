from ajax_select.fields import AutoCompleteSelectMultipleField, AutoCompleteField
from pkg_resources import require
from .models import Shipping
from django import forms


class ShippingForm(forms.ModelForm):
    # supplier = AutoCompleteField(
    #     "suppliers", label="Поставщик", required=False, help_text=None
    # )
    # factory = AutoCompleteField(
    #     "factories", label="Завод", required=False, help_text=None
    # )
    # order = AutoCompleteField("orders", label="Приказ", required=False, help_text=None)
    # seller = AutoCompleteField(
    #     "sellers", label="Продавец", required=False, help_text=None
    # )
    # buyer = AutoCompleteField(
    #     "buyers", label="Покупатель", required=False, help_text=None
    # )
    # product = AutoCompleteField(
    #     "products", label="Продукция", required=False, help_text=None
    # )
    # driver = AutoCompleteField(
    #     "drivers", label="Водитель", required=False, help_text=None
    # )
    # address = AutoCompleteField(
    #     "addresses", label="Адрес", required=False, help_text=None
    # )

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
    # dispatcher = AutoCompleteField(
    #     "dispatcher", label="Диспетчер", required=False, help_text=None
    # )

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
