from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', item_list),
    url(r'^([0-9]+)/$', item_detail),
]
