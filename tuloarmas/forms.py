# -*- encoding: utf-8 -*-

from django import forms
from tuloarmas.models import *

class LoginForm(forms.Form):
    #username = forms.CharField()
    #password = forms.CharField(widget=forms.PasswordInput())
    
    username = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder':'Username'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder':'Password'})
    )

class ComentarioForm(forms.Form):
    texto = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder':'Escribe un comentario...'})
    )
class registroUsuario(forms.Form):

    rut = forms.IntegerField()
    nombre = forms.CharField()
    mail = forms.EmailField()
    telefono = forms.IntegerField()
    pass1 = forms.CharField()
    #Comprobacion del password
    pass2 = forms.CharField()
class tutorialCreationForm(forms.Form):
    nombreTuto = forms.CharField()
    descripcion= forms.CharField()
    HH = forms.IntegerField()
    materialResultante= forms.CharField()
    numProc= forms.IntegerField()