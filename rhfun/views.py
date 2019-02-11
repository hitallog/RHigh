from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .models import Vaga
from django.template import loader
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views import generic
from django.contrib.auth.models import User
from django.views.generic.edit import UpdateView
import requests

from rhfun.forms import CadastrarVagaForm, CadastrarCurriculoForm, CadastrarPessoaForm


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
    return render(request, 'cadastrar_pessoa.html', {'form': form})


def ver_vagas(request):
    vagas_list = Vaga.objects.all()
    context = {'vagas_list': vagas_list}
    return render(request, 'rhfun/vagas.html', context)

def detail(request, vaga_id):
    vaga = Vaga.objects.get(pk=vaga_id)

    filme = requests.get('http://www.omdbapi.com/?t='+vaga.vaga+'&apikey=29eb5528')

    return render(request, 'rhfun/detail.html', {'vaga': vaga, 'filme': filme.json()})

def filme(request):
    return HttpResponse("buscar filme")

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
    return render(request, 'cadastrar_vaga.html', {'form': form})


def cadastrar_curriculo(request):
    if request.method == 'POST':
        form = CadastrarCurriculoForm(request.POST)
        if form.is_valid():
            form.save()
            profile = form.cleaned_data.get('profile')
            formacao = form.cleaned_data.get('formacao')
            experiencia = form.cleaned_data.get('experiencia')
            infos = form.cleaned_data.get('infos')

            return redirect('home')
    else:
        form = CadastrarCurriculoForm()
    return render(request, 'cadastrar_curriculo.html', {'form': form})
            

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


def vote(request, question_id):
    vaga = get_object_or_404(Vaga, pk=question_id)
    try:
        selected_choice = vaga.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'rhfun/detail.html', {
            'vaga': vaga,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.vaga += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('rhfun:results', args=(vaga.id,)))

def results(request, vaga_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % vaga_id)