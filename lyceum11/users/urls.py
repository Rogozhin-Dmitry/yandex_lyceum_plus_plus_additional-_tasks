from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^users/$', user_list),
    url(r'^users/([0-9]+)/$', user_detail),
    url(r'^signup/', signup),
    url(r'^profile/', profile),
]
