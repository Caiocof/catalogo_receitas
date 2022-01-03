from django.db import models

from datetime import datetime

# Create your models here.
class Receitas(models.Model):
    nome = models.CharField(max_length=100)
    ingredientes = models.TextField()
    modo_preparo = models.TextField()
    tempo_preparo = models.IntegerField()
    rendimento = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100)
    data_receita = models.DateTimeField(default=datetime.today(), blank=True)

    class Meta:
        verbose_name = 'Receita'
