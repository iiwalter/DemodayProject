from django.shortcuts import render, get_object_or_404, redirect
from website.forms import CadastroForm
from website.forms import AlagouForm
from website.forms import LoginForm
from website.forms import PesquisaForm
from website.models import *
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Count
# Create your views here.


def layout(request):
    return render(request, 'layout.html')


def home(request):
    form = PesquisaForm(request.POST)
    if form.is_valid():
        locals2 = Alagou.objects.values('rua').annotate(dCount=Count('rua'))
        lugaresCertos = []
        for local in locals2:
            if local.get('dCount') >= 5:
                lugaresCertos.append(local)            
        matches = (lugar for lugar in lugaresCertos if form.cleaned_data['pesquisa'] in lugar.get('rua'))        
        return render(request, 'home.html', {'formulario': form, 'matches': matches})
    return render(request, 'home.html', {'formulario': form})    

@login_required(login_url='/login/')
def alagou(request):
    form = AlagouForm(request.POST or None)
    if form.is_valid():
        form.save()
        context = {
            'msg': "Alagamento cadastrado com sucesso"
        }
        return render(request, 'alagou.html', context)
    context = {
        'formulario': form
    }
    return render(request, 'alagou.html', context)


def cadastro(request):
    form = CadastroForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            # context = {
            #     'msg': "Cadastro efetuado com sucesso"
            # }
        return render(request, 'home.html')
    context = {
        'formulario': form
    }
    return render(request, 'cadastro.html', context)


def local(request):
    locals2 = Alagou.objects.values('rua').annotate(dCount=Count('rua'))
    lugaresCertos = []
    for local in locals2:
        if local.get('dCount') >= 5:
            lugaresCertos.append(local)
    return render(request, 'locaisalagados.html', {'lugaresCertos': lugaresCertos})

def login_user(request):
    # form = LoginForm(request.POST or None)
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(
                username=request.POST['username'], password=request.POST['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('/')
                else:
                    return HttpResponse('Disabled account')
        else:
            return HttpResponse('Invalid Login')
    else:
        form = LoginForm()
    context = {
        'formulario': form
    }
    return render(request, 'login.html', context)

def logout_view(request):
    logout(request)
    return redirect('/')
