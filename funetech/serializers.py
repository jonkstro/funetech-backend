

# /////////////////////////////////////////////////////////////////////////////////////////////////////////////
from django.contrib.auth.models import User, Group
from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from django.contrib.auth import get_user_model
User = get_user_model()

class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    username = serializers.CharField(write_only=True, required=False)
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'first_name', 'is_active']
    
    
    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data.get('password'))
        validated_data['is_active'] = False
        validated_data['username'] = validated_data['email']

        return super(UserCreateSerializer, self).create(validated_data)
