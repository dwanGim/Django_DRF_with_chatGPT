from rest_framework import serializers
from .models import CustomUser

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        # fields = ['name']
        # exclude = ['name']
        fields = '__all__'


