from ajax_select import register, LookupChannel
from .models import Shipping


@register("shippings")
class ShippingsLookup(LookupChannel):

    model = Shipping

    def get_query(self, q, request):
        return self.model.objects.filter(supplier__icontains=q).order_by("supplier")[
            :50
        ]

    def format_item_display(self, item):
        print(item.supplier)
        return "<span class='tag'>%s</span>" % item.supplier
