from .models import HabilidadeRequerida
from .serializers import HabilidadeRequeridaSerializer
from rest_framework.response import Response
from rest_framework import status
from projetos.models import Publicacao
from pesquisadores.models import Pesquisador

from rest_framework.views import APIView
from rest_framework.decorators import api_view

def _cadastrar_habilidade(pub, habilidade, nivel, tipo="publicacao"):
    HabilidadeRequerida.objects.create(publicacao=pub,
                                       habilidade=habilidade,
                                       tipo=tipo,
                                       nivel_da_habilidade=nivel)
    return True

def _get_habilidades_pub(pub):
    habs = HabilidadeRequerida.objects.filter(publicacao=pub, tipo="publicacao")
    return HabilidadeRequeridaSerializer(habs, many=True).data

def _get_habilidades_pesquisador(pesquer):
    habs = HabilidadeRequerida.objects.filter(publicacao=pesquer, tipo="pesquisador")
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
        return Response(_get_habilidades_pub(pub=pub), status=status.HTTP_200_OK)
    
    @api_view(['POST'])
    def pegar_habilidades_pesquer(request):
        dados = request.data
        pesquer = Pesquisador.objects.get(apelido=dados["apelido"])
        return Response(_get_habilidades_pub(pesquer=pesquer), status=status.HTTP_200_OK)