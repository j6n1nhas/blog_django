from django.forms import ModelForm
from .models import Comentario
import requests


class FormComentario(ModelForm):
    def clean(self):
        dados_crus = self.data
        recaptcha_resposta = dados_crus.get('g-recaptcha-response')
        if not recaptcha_resposta:
            self.add_error('comentario', 'Necessário marcar "Não sou um robot"')
        recaptcha_request = requests.post('https://www.google.com/recaptcha/api/siteverify',
                                          data={'secret': '6LcGdB4aAAAAAPLf5cPOF-0xmKmGwb0S095_1hgk',
                                                'response': recaptcha_resposta})
        recaptcha_result = recaptcha_request.json()
        if not recaptcha_result.get('success'):
            self.add_error('comentario', 'Erro no reCAPTCHA')
        data = self.cleaned_data
        nome = data.get('nome_comentario')
        email = data.get('email_comentario')
        comentario = data.get('comentario')
        if len(nome) < 3:
            self.add_error('nome_comentario', 'Nome tem de ter mais que 2 carateres')

    class Meta:
        model = Comentario
        fields = ('nome_comentario', 'email_comentario', 'comentario', )
