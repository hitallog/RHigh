# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.IntegerField(primary_key=True)
    email = models.CharField(max_length=100)
   
    def __str__(self):
        return self.nome

class Curriculo(models.Model):
    profile = models.ForeignKey(Pessoa, on_delete=models.CASCADE)   
    formacao = models.CharField(max_length=200)
    experiencia = models.CharField(max_length=200)
    infos = models.CharField(max_length=200)

    def __str__(self):
        return self.profile

class Vaga(models.Model):
    vaga = models.CharField(max_length=100)
    desc = models.CharField(max_length=200)
    salario = models.IntegerField()

    def __str__(self):
        return self.vaga

