from django.db import models
from categorias.models import Categoria
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.
class Post(models.Model):
    titulo_post = models.CharField('Título', max_length=255, blank=False)
    autor_post = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name='Autor')
    data_post = models.DateTimeField('Data do post', default=timezone.now)
    conteudo_post = models.TextField('Conteúdo', )
    excerto_post = models.TextField('Excerto do post', )
    categoria_post = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING, blank=True, null=True, verbose_name='Categoria do post')
    imagem_post = models.ImageField('Imagem', upload_to='post_images', blank=True)
    publicado_post = models.BooleanField('Publicado', default=False)

    def __str__(self):
        return self.titulo_post