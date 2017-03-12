from django.conf.urls import url, include
from apitry import views
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import routers
from .views import CoursesViewSet, ThemeViewSet, TestViewSet, UserViewSet, GroupViewSet

#urlpatterns = [
#    url(r'^courses/$', views.course_list),
#    url(r'^courses/(?P<pk>[0-9]+)/$', views.course_detail),
#]
#
#urlpatterns = format_suffix_patterns(urlpatterns)

router = routers.DefaultRouter()
router.register(r'courses', CoursesViewSet)
router.register(r'themes', ThemeViewSet)
router.register(r'tests', TestViewSet)
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)

#urlpatterns = [
#    url(r'^', include('rest_framework_swagger.urls')),
#]

urlpatterns = router.urls
