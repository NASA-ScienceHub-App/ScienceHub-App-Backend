from django.db import models
from projetos.models import Publicacao

class HabilidadeRequerida(models.Model):
    NIVEIS = [
        ("Iniciante", "Iniciante"),
        ("Intermediário", "Intermediário"),
        ("Avançado", "Avançado"),
    ]
    publicacao = models.ForeignKey(Publicacao,on_delete=models.CASCADE)
    habilidade = models.CharField(max_length=127, blank=True)
    nivel_da_habilidade = models.CharField(max_length=127, choices=NIVEIS)
    
    class Meta:
            verbose_name = "HabilidadeRequerida"
            verbose_name_plural = "HabilidadeRequerida"
            def __str__(self):
                return self.__all__

