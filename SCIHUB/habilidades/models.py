from django.db import models
from projetos.models import Publicacao
from pesquisadores.models import Pesquisador
class HabilidadeRequerida(models.Model):
    NIVEIS = [
        ("Iniciante", "Iniciante"),
        ("Intermediário", "Intermediário"),
        ("Avançado", "Avançado"),
    ]
    TIPO = [
        ("pesquisador", "pesquisador"),
        ("publicacao", "publicacao")
    ]
    publicacao = models.ForeignKey(Publicacao,on_delete=models.CASCADE, blank=True, null=True)
    pesquisador = models.ForeignKey(Pesquisador,on_delete=models.CASCADE, blank=True, null=True)
    tipo = models.CharField(max_length=127, default="publicacao",choices=TIPO)
    habilidade = models.CharField(max_length=127, blank=True)
    nivel_da_habilidade = models.CharField(max_length=127, choices=NIVEIS)
    
    class Meta:
            verbose_name = "HabilidadeRequerida"
            verbose_name_plural = "HabilidadeRequerida"
            def __str__(self):
                return self.__all__

