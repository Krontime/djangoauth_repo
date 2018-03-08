from django.conf.urls import url, include
from django.contrib import admin
from home.views import get_home_index
from accounts import urls as accounts_urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', get_home_index, name="home"),
    url(r'^accounts/', include(accounts_urls)),
]
