from django.db import models
from django.conf import settings

# Create your models here.
class Servico(models.Model):
    dono = models.ForeignKey(settings.AUTH_USER_MODEL,
                             related_name='servicos',
                             on_delete=models.CASCADE)

    nome = models.CharField(max_length=100, null=False)
    valor = models.FloatField(default=0)

class Produto(models.Model):
    dono = models.ForeignKey(settings.AUTH_USER_MODEL,
                             related_name='produtos',
                             on_delete=models.CASCADE)
    nome = models.CharField(max_length=250, null= False)
    valor = models.FloatField(default=0)
    quantidade = models.IntegerField(default=0)