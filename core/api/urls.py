from django.urls import path
from home.views import index, Person


urlpatterns = [
    path('index/', index),
    path('user/', Person),
]
