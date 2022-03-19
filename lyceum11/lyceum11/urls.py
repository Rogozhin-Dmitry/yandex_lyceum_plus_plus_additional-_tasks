from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^$', include('homepage.urls')),
    url(r'^catalog/', include('catalog.urls')),
    url(r'^about/', include('about.urls')),
    url(r'^auth/', include('users.urls')),
    url(r'^admin/', admin.site.urls),
]
