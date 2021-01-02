from django import template

register = template.Library()


@register.filter(name='coment_plural')
def coment_plural(valor):
    try:
        num_comentarios = int(valor)
        if num_comentarios == 0:
            return 'Nenhum comentário'
        elif num_comentarios == 1:
            return f'{num_comentarios} comentário'
        else:
            return f'{num_comentarios} comentários'
    except:
        return f'{num_comentarios} comentarios'
