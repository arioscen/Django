from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^add_record',views.add_record, name='add_record'),
    url(r'^$', views.post_list, name='post_list'),
]