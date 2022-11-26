from django.contrib.auth.models import User, Group
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'first_name', 'last_name', 'password')
        write_only_fields = ('username',)

    def validate(self, data):
        # Ao inves de utilizar username, irá ser usado o email para autenticação
        email = data.get('email', None)
        if email:
            data['username'] = email
        return data


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['id', 'url', 'name']