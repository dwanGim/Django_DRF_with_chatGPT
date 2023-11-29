from rest_framework import serializers
from .models import Notice, ChatPost

class NoticeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notice
        fields = '__all__'

class ChatPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatPost
        fields = '__all__'