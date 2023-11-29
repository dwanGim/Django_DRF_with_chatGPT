## chat > admin.py
from django.contrib import admin
from .models import Notice, ChatPost

admin.site.register(Notice)
admin.site.register(ChatPost)
