from uuid import uuid4
from django.db import models

# Create your models here.
class Pesquisador(models.Model):
    perfil_publico = models.BooleanField(default=True)
    # id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    nome = models.CharField(max_length=127)
    apelido = models.CharField(primary_key=True, max_length=127, editable=False)
    idade = models.IntegerField()
    entrada_plataforma = models.DateTimeField(auto_now_add=True)
    sobre_mim = models.CharField(max_length=255)
    inidicacoes = models.IntegerField(default=0)
    contra_indicacoes = models.IntegerField(default=0)
    contribuicoes = models.IntegerField(default=0)
    # quais as tags que ele mais contribuiu (top 3 + outros)
    
    class Meta:
            verbose_name = "Pesquisador"
            verbose_name_plural = "Pesquisadores"

            def __str__(self):
                return self.nome
            
# nova tabela para as relacionar habilidades de um pesquisador
# unique_together = ["habilidade", "pesquisador"]