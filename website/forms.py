from django import forms
from website.models import Cadastro
from website.models import Alagou
from django.contrib.auth.models import User


class CadastroForm(forms.ModelForm):
    User._meta.get_field('email').blank = False
    User._meta.get_field('password').blank = False
    password = forms.CharField(max_length=16, widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Senha'}))

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',
        ]
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'maxlength': 140, 'placeholder': 'Username'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'})
        }

    def save(self, commit=True):
        user = super(CadastroForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user


class AlagouForm(forms.ModelForm):
    class Meta:
        model = Alagou
        fields = [
            'rua',
            'bairro',
        ]
        widgets = {
            'rua': forms.TextInput(attrs={'class': 'form-control', 'maxlength': 140, 'placeholder': 'Endereço alagado'}),
            'bairro': forms.TextInput(attrs={'class': 'form-control', 'maxlength': 140, 'placeholder': 'Bairro'}),
        }


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'UserName'}))
    password = forms.CharField(max_length=16, widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Senha'}))


class PesquisaForm(forms.Form):
    pesquisa = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Digite a Rua'}))
