from django import forms
from .models import *

class FornecedorForm(forms.ModelForm):

    class Meta:
        model = Fornecedor
        fields = ['nome', 'rua', 'numero', 'bairro', 'cidade'] 