from django.template.defaulttags import url
from django.urls import path, re_path
# from .views import EscalaView
from .views import HabilidadeApiView

# from .views import EscalaView

urlpatterns = [
    path('cadastrar-habilidade/', HabilidadeApiView.cadastrar_habilidade, name='cadastrar-habilidade'),
    path('pegar-habilidade-pub/', HabilidadeApiView.pegar_habilidades_pub, name='pegar-habilidade-pub'),
    
]