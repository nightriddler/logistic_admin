from operator import index
from django.contrib import admin

from .models import Shipping
from import_export import resources
from import_export.admin import ExportActionMixin, ImportExportModelAdmin, ImportMixin
from import_export.fields import Field
from import_export.widgets import DateWidget
from rangefilter.filters import DateRangeFilter
from django_object_actions import DjangoObjectActions


class ShippingResource(resources.ModelResource):
    # id = Field(attribute="id", column_name="id")
    date = Field(
        attribute="date", column_name="Дата", widget=DateWidget("%d.%m.%Y"), default=""
    )
    supplier = Field(attribute="supplier", column_name="Поставщик")
    factory = Field(attribute="factory", column_name="Завод")
    order = Field(attribute="order", column_name="Приказ")
    seller = Field(attribute="seller", column_name="Продавец")
    buyer = Field(attribute="buyer", column_name="Покупатель")
    waybill = Field(attribute="waybill", column_name="Накладная")
    sales_tax = Field(attribute="sales_tax", column_name="ТТН", default="")
    product = Field(attribute="product", column_name="Продукция")
    quantity = Field(attribute="quantity", column_name="Количество")
    purchase_price = Field(attribute="purchase_price", column_name="Цена покупки")
    sales_price = Field(attribute="sales_price", column_name="Цена продажи")
    delivery_price = Field(attribute="delivery_price", column_name="Цена доставки")
    driver = Field(attribute="driver", column_name="Водитель")
    address = Field(attribute="address", column_name="Адрес")
    dispatcher = Field(attribute="dispatcher", column_name="Диспетчер")
    comment = Field(attribute="comment", column_name="Комментарий", default="")

    class Meta:
        model = Shipping
        exclude = ("id",)
        import_id_fields = (
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
        # export_order = (
        #     "date",
        #     "supplier",
        #     "factory",
        #     "order",
        #     "seller",
        #     "buyer",
        #     "waybill",
        #     "sales_tax",
        #     "product",
        #     "quantity",
        #     "purchase_price",
        #     "sales_price",
        #     "delivery_price",
        #     "driver",
        #     "address",
        #     "dispatcher",
        #     "comment",
        # )
        # exclude = ("id",)
        # import_id_fields = ("date",)

        # widgets = {
        #     "date": {"format": "%d.%M.%Y"},
        # }


from ajax_select.admin import AjaxSelectAdmin


class ShippingAdmin(ImportMixin, ExportActionMixin, AjaxSelectAdmin, admin.ModelAdmin):
    resource_class = ShippingResource
    from .forms import ShippingForm

    form = ShippingForm
    list_display = [
        field.name for field in Shipping._meta.get_fields() if field.name != "id"
    ]

    list_filter = [("date", DateRangeFilter)]
    # + [
    #     field.name
    #     for field in Shipping._meta.get_fields()
    #     if field.name != "id" and field.name != "date"
    # ]
    search_fields = [
        field.name + "__istartswith"
        for field in Shipping._meta.get_fields()
        if field.name != "id" and field.name != "date"
    ]
    # list_editable = ("waybill",)
    resource_class = ShippingResource
    actions = ["clone"]

    # actions_selection_counter = False
    actions_on_bottom = False
    actions_on_top = True
    date_hierarchy = "date"
    list_per_page = 30
    # raw_id_fields = ("supplier",)

    def clone(self, request, queryset):
        from copy import deepcopy

        old_obj = deepcopy(queryset)
        for obj in old_obj:
            obj.id = None
            obj.save()
        self.message_user(request, f"Сделано копий - {len(old_obj)}.")

    clone.short_description = "Копировать"

    def get_actions(self, request):
        actions = super(ShippingAdmin, self).get_actions(request)
        actions["delete_selected"] = (
            actions["delete_selected"][0],
            actions["delete_selected"][1],
            "Удалить",
        )
        actions["export_admin_action"] = (
            actions["export_admin_action"][0],
            actions["export_admin_action"][1],
            "Сохранить документ",
        )
        # if ("delete_selected" or "clone") in actions:
        #     del actions["delete_selected"]
        #     del actions["clone"]
        return actions

    # class Meta:
    #     widgets = {
    #         "date": {"format": "%d.%M.%Y"},
    #     }


admin.site.register(Shipping, ShippingAdmin)
# admin.site.disable_action("delete_selected")
admin.site.site_header = "ТК Авангард"
admin.site.site_title = "Авангард"
# admin.site.index_template = "admin/shipping/shipping/"
# admin.autodiscover()
