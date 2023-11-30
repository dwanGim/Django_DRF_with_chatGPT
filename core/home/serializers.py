from rest_framework import serializers
from .models import CustomUser

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = '__all__'

    def validate(self, data):

        special_characters ="!@#$%^&*()-+?_=,<>/"

        if any(c in special_characters for c in data['name']):
            raise serializers.ValidationError('이름에 특수문자는 허용되지 않습니다.')

        if data['age']<18:
            raise serializers.ValidationError('age는 18세 이상이어야합니다.')

        return data

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()
    