from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router=DefaultRouter() 
router.register('helloview',views.HelloViewSet,basename='helloviewset')


urlpatterns = [
    path('hello/',views.HelloApiView.as_view()),
    path('',include(router.urls)),
 ]
  