from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class PeliculasFormulario(forms.Form):
    nombre =forms.CharField()
    precio= forms.IntegerField()
    imagen= forms.ImageField(required=False)
    estado = forms.CharField()
    genero = forms.CharField()
    descripcion= forms.CharField()
    fecha= forms.DateTimeField()
    vendedor= forms.CharField()
    contacto= forms.CharField()
    

class ComicFormulario(forms.Form):
    nombre= forms.CharField()
    precio= forms.IntegerField()
    imagen= forms.ImageField(required=False)
    estado= forms.CharField()
    editorial= forms.CharField()
    descripcion= forms.CharField()
    fecha=forms.DateTimeField()
    vendedor= forms.CharField()
    contacto= forms.CharField()
    
    
class MusicaFormulario(forms.Form):
    artista= forms.CharField()
    precio= forms.IntegerField()
    imagen= forms.ImageField(required=False)
    disco= forms.CharField()
    genero= forms.CharField()
    estado= forms.CharField()
    descripcion= forms.CharField()
    fecha=forms.DateTimeField()
    vendedor= forms.CharField()
    contacto= forms.CharField()
    

class AvatarFormulario(forms.Form):
    #especificar los campos
    username=forms.ModelChoiceField(queryset=User.objects.all())
    imagen = forms.ImageField(required=True)

    class Meta:
        model = User
        fields = ['imagen']
        help_texts = {k:"" for k in fields}