from django.db import models
from pesquisadores.models import Pesquisador

def upload_to(self, filename):
    # usar filefield
    # ver com a Catarine
    return '/'.join(str(self.name), filename) 

class Projeto(models.Model):
    codigo = models.CharField(primary_key=True, max_length=255, editable=False)
    # nick do criador +( + /)? + nome
    criacao = models.DateTimeField(auto_now_add=True)
    nome = models.CharField(max_length=127)
    descricao = models.CharField(max_length=511)
    # foto
    dono = models.ForeignKey(Pesquisador,on_delete=models.CASCADE, null=True)
    
    class Meta:
            verbose_name = "Projeto"
            verbose_name_plural = "Projetos"
            unique_together = ["dono", "nome"] #TODO ver se e assim msm
            def __str__(self):
                return self.nome
            
class Publicacao(models.Model):
    TIPOS = [
        ("Noticia", "Noticia"),
        ("Recrutamento", "Recrutamento")
    ]
    projeto = models.ForeignKey(Projeto,on_delete=models.CASCADE)
    tipo = models.CharField(max_length=50, choices=TIPOS),
    titulo = models.CharField(max_length=127)
    descricao = models.CharField(max_length=255, blank=True)
    
    class Meta:
            verbose_name = "Publicacao"
            verbose_name_plural = "Publicacoes"
            def __str__(self):
                return self.__all__
