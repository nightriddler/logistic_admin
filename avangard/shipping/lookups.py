from ajax_select import register, LookupChannel
from .models import Shipping


@register("supplier")
class SupplierLookup(LookupChannel):

    model = Shipping

    def get_query(self, q, request):
        return list(
            set(
                [
                    result.supplier
                    for result in self.model.objects.filter(
                        supplier__icontains=q
                    ).order_by("supplier")[:50]
                ]
                + [
                    result.supplier
                    for result in self.model.objects.filter(
                        supplier__icontains=q.capitalize()
                    ).order_by("supplier")[:50]
                ]
            )
        )

    def format_item_display(self, item):
        return "<span class='tag'>%s</span>" % item


@register("factory")
class SupplierLookup(LookupChannel):

    model = Shipping

    def get_query(self, q, request):
        return list(
            set(
                [
                    result.factory
                    for result in self.model.objects.filter(
                        factory__icontains=q
                    ).order_by("factory")[:50]
                ]
                + [
                    result.factory
                    for result in self.model.objects.filter(
                        factory__icontains=q.capitalize()
                    ).order_by("factory")[:50]
                ]
            )
        )

    def format_item_display(self, item):
        return "<span class='tag'>%s</span>" % item


@register("order")
class SupplierLookup(LookupChannel):

    model = Shipping

    def get_query(self, q, request):
        return list(
            set(
                [
                    result.order
                    for result in self.model.objects.filter(
                        order__icontains=q
                    ).order_by("order")[:50]
                ]
                + [
                    result.order
                    for result in self.model.objects.filter(
                        order__icontains=q.capitalize()
                    ).order_by("order")[:50]
                ]
            )
        )

    def format_item_display(self, item):
        return "<span class='tag'>%s</span>" % item


@register("seller")
class SupplierLookup(LookupChannel):

    model = Shipping

    def get_query(self, q, request):
        return list(
            set(
                [
                    result.seller
                    for result in self.model.objects.filter(
                        seller__icontains=q
                    ).order_by("seller")[:50]
                ]
                + [
                    result.seller
                    for result in self.model.objects.filter(
                        seller__icontains=q.capitalize()
                    ).order_by("seller")[:50]
                ]
            )
        )

    def format_item_display(self, item):
        return "<span class='tag'>%s</span>" % item


@register("buyer")
class SupplierLookup(LookupChannel):

    model = Shipping

    def get_query(self, q, request):
        return list(
            set(
                [
                    result.buyer
                    for result in self.model.objects.filter(
                        buyer__icontains=q
                    ).order_by("buyer")[:50]
                ]
                + [
                    result.buyer
                    for result in self.model.objects.filter(
                        buyer__icontains=q.capitalize()
                    ).order_by("buyer")[:50]
                ]
            )
        )

    def format_item_display(self, item):
        return "<span class='tag'>%s</span>" % item


@register("product")
class SupplierLookup(LookupChannel):

    model = Shipping

    def get_query(self, q, request):
        return list(
            set(
                [
                    result.product
                    for result in self.model.objects.filter(
                        product__icontains=q
                    ).order_by("product")[:50]
                ]
                + [
                    result.product
                    for result in self.model.objects.filter(
                        product__icontains=q.capitalize()
                    ).order_by("product")[:50]
                ]
            )
        )

    def format_item_display(self, item):
        return "<span class='tag'>%s</span>" % item


@register("driver")
class SupplierLookup(LookupChannel):

    model = Shipping

    def get_query(self, q, request):
        return list(
            set(
                [
                    result.driver
                    for result in self.model.objects.filter(
                        driver__icontains=q
                    ).order_by("driver")[:50]
                ]
                + [
                    result.driver
                    for result in self.model.objects.filter(
                        driver__icontains=q.capitalize()
                    ).order_by("driver")[:50]
                ]
            )
        )

    def format_item_display(self, item):
        return "<span class='tag'>%s</span>" % item


@register("address")
class SupplierLookup(LookupChannel):

    model = Shipping

    def get_query(self, q, request):
        return list(
            set(
                [
                    result.address
                    for result in self.model.objects.filter(
                        address__icontains=q
                    ).order_by("address")[:50]
                ]
                + [
                    result.address
                    for result in self.model.objects.filter(
                        address__icontains=q.capitalize()
                    ).order_by("address")[:50]
                ]
            )
        )

    def format_item_display(self, item):
        return "<span class='tag'>%s</span>" % item


@register("dispatcher")
class SupplierLookup(LookupChannel):

    model = Shipping

    def get_query(self, q, request):
        return list(
            set(
                [
                    result.dispatcher
                    for result in self.model.objects.filter(
                        dispatcher__icontains=q
                    ).order_by("dispatcher")[:50]
                ]
                + [
                    result.dispatcher
                    for result in self.model.objects.filter(
                        dispatcher__icontains=q.capitalize()
                    ).order_by("dispatcher")[:50]
                ]
            )
        )

    def format_item_display(self, item):
        return "<span class='tag'>%s</span>" % item
