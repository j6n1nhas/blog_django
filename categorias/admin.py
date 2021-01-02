from django.contrib import admin
from .models import Categoria


# Register your models here.
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome')
    list_display_links = ('id', 'nome')
    search_fields = ('nome', )


admin.site.register(Categoria, CategoriaAdmin)
