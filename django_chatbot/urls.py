
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include('chatbot.urls'))
    path('accounts/', include('accountapp.urls')),
    path('api-auth/', include('rest_framework.urls')),
]
