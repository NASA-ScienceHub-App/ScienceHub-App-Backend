from rest_framework import serializers
from .models import HabilidadeRequerida

class HabilidadeRequeridaSerializer(serializers.ModelSerializer):
    class Meta:
        model = HabilidadeRequerida
        fields = '__all__'