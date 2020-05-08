from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router=DefaultRouter() 
router.register('helloview',views.HelloViewSet,basename='helloviewset')
router.register('profile',views.UserProfileViewSet)   
"""basename not needed if have a queryset"""

urlpatterns = [
    path('hello/',views.HelloApiView.as_view()),
    path('login/',views.UserLoginApiView.as_view()),
    path('',include(router.urls)),
 ]
  