from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.core.exceptions import ValidationError
from rest_framework.authtoken.models import Token

class UserCreateSerializer(serializers.ModelSerializer):
    token = serializers.CharField(allow_blank=True, read_only=True)
    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'token']
        extra_kwargs = {
            "password": {
                "write_only": True
            }
        }

    def create(self, validated_data):
        username = validated_data['username']
        password = validated_data['password']
        email = validated_data['email']

        user = User(username=username, email=email)
        user.set_password(password)
        user.save()

        token = Token.objects.create(user=user)
        validated_data['token'] = token.key

        return validated_data

class UserLoginSerializer(serializers.ModelSerializer):
    token = serializers.CharField(allow_blank=True, read_only=True)
    username = serializers.CharField()

    class Meta:
        model = User
        fields = ['username', 'password', 'token']
        extra_kwargs = {
            "password": {
                "write_only": True
            }
        }

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            data['token'] = 'some random token'
        else:
            raise ValidationError('wrong username or password')

        token = Token.objects.filter(user=user)

        data['token'] = token.first().key

        return data
