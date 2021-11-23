from django.forms import ModelForm
from .models import ControleCaixa

class FieldsApp(ModelForm):
    class Meta:
        model = ControleCaixa
        fields = ['saida', 'entrada', 'data_fluxo']
