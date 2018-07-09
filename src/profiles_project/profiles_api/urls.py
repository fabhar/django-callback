from django.conf.urls import url
from django.conf.urls import include

from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('token/getToken', views.GetTokenViewSet, base_name='getToken')
router.register('profile', views.UserProfileViewSet)
router.register('login', views.LoginViewSet, base_name='login')
router.register('feed', views.UserProfileFeedViewSet)

urlpatterns = [
    url(r'^hello-view/', views.HelloApiView.as_view()),
    url(r'', include(router.urls))
]
