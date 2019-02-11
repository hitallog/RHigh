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




def cadastrar(request):
    return HttpResponse("Area de cadastro do cliente.")

def ver_vagas(request):
    vagas_list = Vaga.objects.all()
    context = {'vagas_list': vagas_list}
    return render(request, 'rhfun/vagas.html', context)

def detail(request, vaga_id):
    vaga = get_object_or_404(Vaga, pk=vaga_id)
    return render(request, 'rhfun/detail.html', {'vaga': vaga})

def cadastrar_vaga(request):
    return HttpResponse("Cadastrar vaga.")

def cadastrar_curriculo(request):
    return HttpResponse("Aqui sera o cadastro de curriculos.")

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