from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .models import Vaga
from rhfun.forms import CadastrarVagaForm, CadastrarCurriculoForm, CadastrarPessoaForm
import requests


def cadastrar(request):
    if request.method == 'POST':
        form_user = UserCreationForm(request.GET)
        form = CadastrarPessoaForm(request.POST)
        if form.is_valid():
            form.save()
            nome = form_user['username'].value()
            nickname = form.cleaned_data.get('nickname')
            cpf = form.cleaned_data.get('cpf')
            email = form.cleaned_data.get('email')
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, '../templates/rhfun/cadastrar_pessoa.html', {'form': form})


def ver_vagas(request):
    vagas_list = Vaga.objects.all()
    context = {'vagas_list': vagas_list}
    return render(request, '../templates/rhfun/vagas.html', context)


def detail(request, vaga_id):
    vaga = Vaga.objects.get(pk=vaga_id)

    filme = requests.get('http://www.omdbapi.com/?t='+vaga.vaga+'&apikey=29eb5528')

    return render(request, '../templates/rhfun/detail.html', {'vaga': vaga, 'filme': filme.json()})


def cadastrar_vaga(request):
    if request.method == 'POST':
        form = CadastrarVagaForm(request.POST)
        if form.is_valid():
            form.save()
            vaga = form.cleaned_data.get('vaga')
            desc = form.cleaned_data.get('desc')
            salario = form.cleaned_data.get('salario')
            
            return redirect('home')
    else:
        form = CadastrarVagaForm()
    return render(request, '../templates/rhfun/cadastrar_vaga.html', {'form': form})


def cadastrar_curriculo(request):
    if request.method == 'POST':
        form = CadastrarCurriculoForm(request.POST)
        if form.is_valid():
            form.save()
            profile = form.cleaned_data.get('profile')
            formacao = form.cleaned_data.get('formacao')
            experiencia = form.cleaned_data.get('experiencia')
            infos = form.cleaned_data.get('infos')

            return redirect('../templates/rhfun/home')
    else:
        form = CadastrarCurriculoForm()
    return render(request, '../templates/rhfun/cadastrar_curriculo.html', {'form': form})


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('../templates/rhfun/home')
    else:
        form = UserCreationForm()
    return render(request, '../templates/rhfun/signup.html', {'form': form})


