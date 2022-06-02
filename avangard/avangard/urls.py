from django.contrib import admin
from django.urls import path, re_path
from ajax_select import urls as ajax_select_urls
from django.conf.urls import include

admin.autodiscover()

urlpatterns = [
    re_path(r"^ajax_select/", include(ajax_select_urls)),
    path("admin/", admin.site.urls),
]
