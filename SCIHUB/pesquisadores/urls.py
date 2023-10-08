from django.template.defaulttags import url
from django.urls import path, re_path
# from .views import EscalaView
from .views import PesquisadorApiView

# from .views import EscalaView

urlpatterns = [
    path('cadastrar-pesquisador/', PesquisadorApiView.cadastrar_pesquisador, name='cadastrar-pesquisador'),
    path('pegar-pesquisador/', PesquisadorApiView.pegar_pesquisador, name='pegar-pesquisador'),
    path('adicionar-indicacao-pesquisador/', PesquisadorApiView.adicionar_indicacao_pesquisador, name='adicionar-indicacao-pesquisador'),
    path('adicionar-contra_indicacao-pesquisador/', PesquisadorApiView.adicionar_contra_indicacao_pesquisador, name='adicionar-contra-indicacao-pesquisador'),
    path('adicionar-contribuicao-pesquisador/', PesquisadorApiView.adicionar_contribuicao_pesquisador, name='adicionar-contribuicao-pesquisador'),
    
]