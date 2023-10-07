from rest_framework import serializers
from .models import Pesquisador

class PesquisadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pesquisador
        fields = '__all__'