from django.template.defaulttags import url
from django.urls import path, re_path
from .views import ProjetoApiView
from .views import PublicacaoApiView

urlpatterns = [
    path('cadastrar-projeto/', ProjetoApiView.cadastrar_projeto, name='cadastrar-projeto'),
    path('atualizar-projeto/', ProjetoApiView.atualizar_projeto, name='atualizar-projeto'),
    path('pegar-projeto/', ProjetoApiView.pegar_projeto, name='pegar-projeto'),
    path('pegar-projetos-pesquisador/', ProjetoApiView.pegar_projetos_pesquisador, name='pegar-projetos-pesquisador'),
    
    path('cadastrar-publicacao/', PublicacaoApiView.cadastrar_publicacao, name='cadastrar-publicacao'),
    path('feed-pesquisador/', PublicacaoApiView.pegar_pubs_feed_pesquisador, name='pegar-pubs-feed-pesquisador'),
    path('publicacao-projeto/', PublicacaoApiView.pegar_pubs_proj, name='pegar-pubs-proj'),
    
]