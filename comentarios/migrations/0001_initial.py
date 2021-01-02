# Generated by Django 3.1.4 on 2021-01-01 19:12

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('posts', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_comentario', models.CharField(max_length=150, verbose_name='Nome do comentário')),
                ('email_comentario', models.EmailField(max_length=254, verbose_name='Email do comentário')),
                ('comentario', models.TextField(verbose_name='Comentário')),
                ('data_comentario', models.DateTimeField(default=datetime.datetime(2021, 1, 1, 19, 12, 44, 31399, tzinfo=utc), verbose_name='Data do comentário')),
                ('publicado_comentario', models.BooleanField(default=False)),
                ('post_comentario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.post')),
                ('utilizador_comentario', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
