from .models import Projeto
from .models import Publicacao
from .serializers import ProjetoSerializer
from .serializers import PublicacaoSerializer
from rest_framework.response import Response
from rest_framework import status
from pesquisadores.models import Pesquisador
from habilidades.views import _cadastrar_habilidade
from habilidades.views import _get_habilidades_pub
# Create your views here.

from rest_framework.views import APIView
from rest_framework.decorators import api_view

class ProjetoApiView(APIView):
    @api_view(['POST'])
    def cadastrar_projeto(request):
        dados = request.data
        pesquer = Pesquisador.objects.get(apelido=dados["apelido"])
        code = str(pesquer.apelido) + str(dados["nome"])
        proj =  Projeto.objects.create(codigo=code,
                                nome=dados["nome"],
                                descricao=dados["descricao"],
                                dono=pesquer)
        return Response("Project created", status=status.HTTP_201_CREATED)
    
    @api_view(['POST'])
    def atualizar_projeto(request):
        dados = request.data
        data = {}
        data["nome"] = dados["nome"]
        pesquer = Pesquisador.objects.get(apelido=dados["apelido"])
        proj = Projeto.objects.get(dono=pesquer, nome=dados["nome"])
        if "novo_nome" in dados:
            data["nome"] = dados["novo_nome"]
        if "nova_descricao" in dados:
            data["descricao"] = dados["descricao"]
        serializer = ProjetoSerializer(proj, data=data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @api_view(['POST'])
    def pegar_projeto(request):
        dados = request.data
        pesquer = Pesquisador.objects.get(apelido=dados["apelido"])
        proj = Projeto.objects.get(dono=pesquer, nome=dados["nome"])
        serializer = ProjetoSerializer(proj, context={'request': request}, many=False)
        return Response(serializer.data)

    @api_view(['POST'])
    def pegar_projetos_pesquisador(request):
        dados = request.data
        pesquer = Pesquisador.objects.get(apelido=dados["apelido"])
        proj = Projeto.objects.filter(dono=pesquer)
        serializer = ProjetoSerializer(proj, context={'request': request}, many=True)
        return Response(serializer.data)
    
    @api_view(['POST'])
    def apagar_projetos(request):
        pass
    
class PublicacaoApiView(APIView):
    @api_view(['POST'])
    def cadastrar_publicacao(request):
        dados = request.data
        proj = Projeto.objects.get(codigo=dados["projeto"])
        pub = Publicacao.objects.create(projeto=proj,
                                         tipo=dados["tipo"],
                                         titulo=dados["titulo"],
                                         descricao=dados["descricao"],
                                         )
        for (habilidade, nivel) in zip(dados["habilidades"], dados["niveis"]):
            _cadastrar_habilidade(pub, habilidade, nivel)
            
        return Response("Publicacao created", status=status.HTTP_201_CREATED)
    
    @api_view(['POST'])
    def pegar_pubs_feed_pesquisador(request):
        dados = request.data
        pesquer = Pesquisador.objects.get(apelido=dados["apelido"])
        proj = Projeto.objects.filter()
        pubs = Publicacao.objects.filter(projeto__in=proj)
        pubs_feed = []
        for pub in pubs:
            json = {}
            json["projeto"] = pub.projeto.codigo
            proj = pub.projeto
            pesquer = proj.dono
            json["autor"] = pesquer.nome
            json["tipo"] = pub.tipo
            json["titulo"] = pub.titulo
            json["descricao"] = pub.descricao
            json["habilidades"] = _get_habilidades_pub(pub=pub)
            pubs_feed.append(json)

        return Response(pubs_feed, status=status.HTTP_200_OK)
    
    @api_view(['POST'])
    def pegar_pubs_proj(request):
        dados = request.data
        proj = Projeto.objects.get(codigo=dados["codigo"])
        pesquer = proj.dono
        pubs = Publicacao.objects.filter(projeto__in=proj, tipo="Recrutamento")
        pubs_proj = []
        for pub in pubs:
            json = {}
            json["projeto"] = pub.projeto.codigo
            json["nome_projeto"] = proj.nome
            json["autor"] = pesquer.nome
            json["tipo"] = pub.tipo
            json["titulo"] = pub.titulo
            json["descricao"] = pub.descricao
            json["habilidades"] = _get_habilidades_pub(pub=pub)
            pubs_proj.append(json)
            
        return Response(pubs_proj, status=status.HTTP_200_OK)
