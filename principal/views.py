from django.shortcuts import render
from principal.models import *
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from principal.forms import *

@login_required
def inicio(request):
    avatares = Avatar.objects.filter(user=request.user.id)
    return render(request, 'principal/inicio.html', {'url':avatares[0].imagen.url})

def about(request):
    return render(request, "principal/about.html")




def comics(request):
    return render(request, "principal/inicio.html")

def musica(request):
    return render(request, "principal/inicio.html")



class PeliculaList(ListView):
    model= Pelicula
    template_name= "principal/peliculas_list.html"
    
class PeliculaDetalle(DetailView):
    model= Pelicula
    template_name= "principal/pelicula_detalle.html"   

class CrearPelicula(LoginRequiredMixin,CreateView):
    model= Pelicula
    template_name = "principal/peliculas.html"
    success_url= reverse_lazy('Pelicula_List')
    
class PeliculaUpdate(UpdateView):
    model= Pelicula
    success_url= reverse_lazy('Pelicula_List') 
    fields='__all__'
    
class DeletePelicula(LoginRequiredMixin,DeleteView):
    model= Pelicula
    success_url= reverse_lazy('Pelicula_List')  
    
    
def peliculas(request):
    if request.method == 'POST':
        miFormulario= PeliculasFormulario(request.POST,request.FILES)
        print(miFormulario)
        
        if miFormulario.is_valid :
        
            informacion= miFormulario.cleaned_data
            pelicula= Pelicula ( nombre=informacion['nombre'],precio =informacion['precio'],imagen=informacion['imagen'],estado =informacion['estado'], genero =informacion['genero'], descripcion =informacion['descripcion'],fecha=informacion['fecha'],vendedor=informacion['vendedor'],contacto =informacion['contacto'])
            pelicula.save()
            return render(request, "principal/inicio.html")
    else:
        miFormulario= PeliculasFormulario()
        
    return render(request, "principal/peliculas.html", {"miFormulario": miFormulario})


def comics(request):
    if request.method == 'POST':
        miFormulario= ComicFormulario(request.POST,request.FILES)
        print(miFormulario)
        
        if miFormulario.is_valid :
        
            informacion= miFormulario.cleaned_data
            comic= Comic ( nombre=informacion['nombre'],precio =informacion['precio'],imagen=informacion['imagen'],estado=informacion['estado'], editorial =informacion['editorial'],descripcion =informacion['descripcion'],fecha=informacion['fecha'],vendedor=informacion['vendedor'],contacto =informacion['contacto'])
            comic.save()
            return render(request, "principal/inicio.html")
    else:
        miFormulario= ComicFormulario()
        
    return render(request, "principal/comics.html", {"miFormulario": miFormulario})


def musica(request):
    if request.method == 'POST':
        miFormulario= MusicaFormulario(request.POST,request.FILES)
        print(miFormulario)
        
        if miFormulario.is_valid :
        
            informacion= miFormulario.cleaned_data
            musica= Comic ( artista=informacion['artista'],precio =informacion['precio'],imagen=informacion['imagen'],disco =informacion['disco'], genero =informacion['genero'], estado=informacion['estado'],descripcion =informacion['descripcion'],fecha=informacion['fecha'],vendedor=informacion['vendedor'],contacto =informacion['contacto'])
            musica.save()
            return render(request, "principal/inicio.html")
    else:
        miFormulario= ComicFormulario()
        
    return render(request, "principal/comics.html", {"miFormulario": miFormulario})



class ComicList(LoginRequiredMixin,ListView):
    model= Comic
    template_name= "principal/comics_list.html"
    
class ComicDetalle(LoginRequiredMixin,DetailView):
    model= Comic
    template_name= "principal/comic_detalle.html"
    
class CrearComic(LoginRequiredMixin,CreateView):
    model= Comic
    template_name = "principal/comics.html"
    success_url= reverse_lazy('Comic_List')
    
class MusicaList(LoginRequiredMixin,ListView):
    model= Musica
    template_name= "principal/musica_list.html"
    
class MusicaDetalle(LoginRequiredMixin,DetailView):
    model= Musica
    template_name= "principal/musica_detalle.html"
    
class CrearMusica(LoginRequiredMixin,CreateView):
    model= Musica
    template_name = "principal/musica.html"
    success_url= reverse_lazy('musica_List')