from django.conf.urls import url, include

from simple_users import views

from rest_framework.routers import DefaultRouter

# API router
router = DefaultRouter()
router.register(r'users', views.UserViewSet)

# finish up
urlpatterns = [
  url(r'^', include(router.urls)),
  url(r'^api-auth/', include('rest_framework.urls',
    namespace='rest_framework')),
]
