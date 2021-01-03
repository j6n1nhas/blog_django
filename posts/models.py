from django.db import models
from categorias.models import Categoria
from django.contrib.auth.models import User
from django.utils import timezone
from PIL import Image
from django.conf import settings
import os


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

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.redimensionar_imagens(self.imagem_post.name, 800)

    @staticmethod
    def redimensionar_imagens(nome_imagem, largura_permitida):
        img_path = os.path.join(settings.MEDIA_ROOT, nome_imagem)
        img = Image.open(img_path)
        largura, altura = img.size
        nova_altura = round((largura_permitida * altura) / largura)
        if largura <= largura_permitida:
            img.close()
            return
        nova_imagem = img.resize((largura_permitida, nova_altura), Image.ANTIALIAS)
        nova_imagem.save(img_path, optimize=True, quality=60)
        nova_imagem.close()