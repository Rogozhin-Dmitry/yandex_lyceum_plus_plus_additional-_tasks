from django.conf.urls import url
from .views import item_list, item_detail

urlpatterns = [
    url(r'^$', item_list),
    url(r'^([0-9]+)/$', item_detail),
]
