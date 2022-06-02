from ajax_select import register, LookupChannel
from .models import Shipping


@register("suppliers")
class SupplierLookup(LookupChannel):

    model = Shipping

    def get_query(self, q, request):
        print("get_query")
        return list(
            set(
                [
                    result.supplier
                    for result in self.model.objects.filter(
                        supplier__icontains=q
                    ).order_by("supplier")[:50]
                ]
            )
        )

    def format_item_display(self, item):
        print("format_item_display")
        print(item)
        return "<span class='tag'>%s</span>" % item
