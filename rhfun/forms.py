from django import forms
from .models import Vaga, Curriculo, Pessoa


class CadastrarVagaForm(forms.ModelForm):
    class Meta:
        model = Vaga
        fields = ['vaga', 'desc', 'salario']

    def __init__(self, *args, **kwargs):
        super(CadastrarVagaForm, self).__init__(*args, **kwargs)
        self.fields['desc'].label = "Descrição"
        self.fields['salario'].label = "Salário"


class CadastrarCurriculoForm(forms.ModelForm):
    class Meta:
        model = Curriculo
        fields = ['profile', 'formacao', 'experiencia', 'infos']
    
    def __init__(self, *args, **kwargs):
        super(CadastrarCurriculoForm, self).__init__(*args, **kwargs)
        self.fields['profile'].label = "Usuário"
        self.fields['formacao'].label = "Formação"
        self.fields['experiencia'].label = "Experiência"
        self.fields['infos'].label = "Informações"


class CadastrarPessoaForm(forms.ModelForm):
    class Meta:
        model = Pessoa
        fields = ['nome', 'cpf', 'email']
