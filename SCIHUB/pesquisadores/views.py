from .models import Pesquisador
from .serializers import PesquisadorSerializer
from rest_framework.response import Response
from rest_framework import status
from pesquisadores.models import Pesquisador
# Create your views here.

from rest_framework.views import APIView
from rest_framework.decorators import api_view

class PesquisadorApiView(APIView):
    @api_view(['POST'])
    def cadastrar_pesquisador(request):
        dados = request.data
        # perfil_publico
        # nome 
        # apelido
        # idade
        # sobre_mim
        # inidicacoes
        # contra_indicacoes
        # contribuicoes
        proj =  Pesquisador.objects.create(perfil_publico = dados["perfil_publico"],
                                        nome = dados["nome"],
                                        apelido = dados["apelido"],
                                        idade = dados["idade"],
                                        sobre_mim = dados["sobre_mim"])
        return Response("Pesquisador created", status=status.HTTP_201_CREATED)
    
    @api_view(['POST'])
    def atualizar_pesquisador(request):
        #TODO: implement
        pass
    
    @api_view(['POST'])
    def adicionar_indicacao_pesquisador(request):
        #TODO: implement
        pass
    
    @api_view(['POST'])
    def adicionar_contra_indicacao_pesquisador(request):
        #TODO: implement
        pass
    
    @api_view(['POST'])
    def adicionar_contribuicao_pesquisador(request):
        #TODO: implement
        pass
    
    @api_view(['POST'])
    def pegar_pesquisador(request):
        dados = request.data
        data = {}
        pesquer = Pesquisador.objects.get(apelido=dados["apelido"])
        serializer = PesquisadorSerializer(pesquer, context={'request': request}, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    @api_view(['POST'])
    def apagar_pesquisador(request):
        pass