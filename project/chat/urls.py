# # chat > urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import NoticeViewSet, ChatPostViewSet

router = DefaultRouter()
router.register(r'notice', NoticeViewSet)
router.register(r'chat', ChatPostViewSet)

urlpatterns = [
    path('', include(router.urls)),
]