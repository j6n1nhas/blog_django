from django.db import models


# Create your models here.
class Categoria(models.Model):
    nome = models.CharField('Categoria', max_length=50, blank=False, unique=True)

    def __str__(self):
        return self.nome