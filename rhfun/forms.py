from django import forms
from .models import Vaga, Curriculo, Pessoa

class CadastrarVagaForm(forms.ModelForm):
    class Meta:
        model = Vaga
        fields = ['vaga', 'desc', 'salario']

class CadastrarCurriculoForm(forms.ModelForm):
    class Meta:
        model = Curriculo
        fields = ['profile', 'formacao', 'experiencia', 'infos']

class CadastrarPessoaForm(forms.ModelForm):
    class Meta:
        model = Pessoa
        fields = ['nome', 'cpf', 'email']
