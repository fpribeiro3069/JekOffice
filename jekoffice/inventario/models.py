from django.db import models

# Create your models here.

# Model muito básico.
# Depois pode ser acrescentado mais detalhes se for necessário
class Item(models.Model):
    nome = models.CharField(max_length=70)
    quantidade = models.IntegerField()

    def __str__(self):
        return "%s: %s" % (self.nome, self.quantidade)
