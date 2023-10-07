from rest_framework import serializers
from .models import Projeto
from .models import Publicacao
class ProjetoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projeto
        fields = '__all__'
        
class PublicacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publicacao
        fields = '__all__'
