from django.db import models
from posts.models import Post
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
class Comentario(models.Model):
    nome_comentario = models.CharField('Nome do comentador', max_length=150)
    email_comentario = models.EmailField('Email do comentador')
    comentario = models.TextField('Comentário')
    post_comentario = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='Post')
    utilizador_comentario = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=True, null=True)
    data_comentario = models.DateTimeField('Data do comentário', default=timezone.now())
    publicado_comentario = models.BooleanField(default=False)

    def __str__(self):
        return self.nome_comentario
