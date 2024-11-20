from django.urls import  path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet,TagViewSet,TaskViewSet



router = DefaultRouter()
router.register('users',UserViewSet)
router.register('tags',TagViewSet)
router.register('tasks',TaskViewSet)


urlpatterns = [
    path('',include(router.urls)),
]