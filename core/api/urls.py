from django.urls import path, include
from home.views import index, Person, login, UserAPI, UserViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='users')
urlpatterns = router.urls



urlpatterns = [
    path('', include(router.urls)),
    path('index/', index),
    path('user/', Person),
    path('login/', login),
    path('users/', UserAPI.as_view())
]
