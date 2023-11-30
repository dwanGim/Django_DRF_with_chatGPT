from django.urls import path
from home.views import index, Person, login


urlpatterns = [
    path('index/', index),
    path('user/', Person),
    path('login/', login),
]
