from django.conf.urls import url
from .views import test, error

urlpatterns = [
    url(r'^login/', test),
    url(r'^signup/', test),
    url(r'^question/(?:<id>\d+)/', test),
    url(r'^ask/', test),
    url(r'^popular/', test),
    url(r'^new/', test),
    url(r'^$', test)
]
