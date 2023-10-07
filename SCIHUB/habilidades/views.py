from .models import HabilidadeRequerida
from .serializers import HabilidadeRequeridaSerializer
from rest_framework.response import Response
from rest_framework import status
from projetos.models import Publicacao

from rest_framework.views import APIView
from rest_framework.decorators import api_view

def _cadastrar_habilidade(pub, habilidade, nivel):
    HabilidadeRequerida.objects.create(publicacao=pub,
                                       habilidade=habilidade,
                                       nivel_da_habilidade=nivel)
    return True
    
def _get_habilidades_pub(pub):
    habs = HabilidadeRequerida.objects.filter(publicacao=pub)
    return HabilidadeRequeridaSerializer(habs, many=True).data
    

class HabilidadeApiView(APIView):
    @api_view(['POST'])
    def cadastrar_habilidade(request):
        dados = request.data
        pub = Publicacao.objects.get(codigo=dados["publicacao"])
        _cadastrar_habilidade(pub, dados["habilidade"], dados["nivel"])
        return Response("Project created", status=status.HTTP_201_CREATED)
    
    @api_view(['POST'])
    def pegar_habilidades_pub(request):
        dados = request.data
        pub = Publicacao.objects.get(codigo=dados["publicacao"])
        return Response(_get_habilidades_pub(), status=status.HTTP_200_OK)