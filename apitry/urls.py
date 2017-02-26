from django.conf.urls import url
from apitry import views

urlpatterns = [
    url(r'^courses/$', views.cours_list),
    url(r'^courses/(?P<pk>[0-9]+)/$', views.cours_detail),
]
