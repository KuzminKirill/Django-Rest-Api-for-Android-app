from rest_framework import routers

from .views import CoursesViewSet, ThemeViewSet, TestViewSet, UserViewSet, GroupViewSet, QuestionViewSet

# urlpatterns = [
#    url(r'^courses/$', views.course_list),
#    url(r'^courses/(?P<pk>[0-9]+)/$', views.course_detail),
# ]
#
# urlpatterns = format_suffix_patterns(urlpatterns)

router = routers.DefaultRouter()
router.register(r'courses', CoursesViewSet)
router.register(r'themes', ThemeViewSet)
router.register(r'tests', TestViewSet)
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'questions', QuestionViewSet)

# urlpatterns = [
#    url(r'^/(?P<username>[0-9a-zA-Z_-]+)$', UserDetail.as_view(), name='user-detail'),
# ]

urlpatterns = router.urls
