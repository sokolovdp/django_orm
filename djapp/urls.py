from django.conf.urls import url
from . import views

app_name = 'djapp'

urlpatterns = [
    url(r'^$', views.ItemListView.as_view(), name='list'),
    url(r'^(?P<pk>\d+)/$', views.ItemDetailView.as_view(), name='detail'),
]
