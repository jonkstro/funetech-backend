from rest_framework import serializers
from .models import Homenagem


class HomenagemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Homenagem
        fields = '__all__'