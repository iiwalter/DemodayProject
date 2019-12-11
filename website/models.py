from django.db import models
from django import forms
from django.contrib.auth.models import User

# Create your models here.
class Cadastro(models.Model):
    nome = models.CharField(max_length=140)
    email = models.EmailField()
    senha = models.CharField(max_length=255)
    widgets = {
        'password':forms.PasswordInput(attrs={'class': 'form-control', 'maxlength':255 })
    }
    def __str__(self):
        return self.nome
class Alagou(models.Model):
    rua = models.CharField(max_length=300)
    bairro = models.CharField(max_length=200)
    def __str__(self):
        return self.bairro


