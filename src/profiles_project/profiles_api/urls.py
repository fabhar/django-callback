from django.conf.urls import url
from django.conf.urls import include

from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('token/getToken', views.GetTokenViewSet, base_name='getToken')
router.register('collect/sendAlarm', views.SendAlarmViewSet, base_name='sendAlarm')
router.register('collect/sendFault', views.SendFaultViewSet, base_name='sendFault')

urlpatterns = [
    url(r'^hello-view/', views.HelloApiView.as_view()),
    url(r'', include(router.urls))
]
