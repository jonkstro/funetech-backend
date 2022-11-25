from rest_framework import serializers
from .models import Homenagem


class HomenagemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Homenagem
        fields = ['id','name', 'user']