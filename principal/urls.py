from django.urls import path
from principal import views
from.views import *
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', views.inicio, name='Inicio'),
    path('peliculas', views.peliculas, name='Peliculas'),
    path('about', views.about, name='About'),
    path('comics', views.comics, name='Comics'),
    path('musica', views.musica, name='Musica'),
    path('logout', LogoutView.as_view(template_name='principal/logout.html'), name='Logout'),
    
    
    
    path('peliculas/list', PeliculaList.as_view(), name= 'Pelicula_List'),
    path('pelicula/nuevo', CrearPelicula.as_view(), name='Pelicula_New'),
    path('pelicula/<pk>', PeliculaDetalle. as_view(), name= 'Pelicula_Detail'),
    path('pelicula/editar/<pk>',PeliculaUpdate.as_view(), name='Pelicula_Edit'),
    path('pelicula/borrar/<pk>', DeletePelicula.as_view(), name='Pelicula_Delete'),
    
    path('comics/list', ComicList.as_view(), name= 'Comic_List'),
    path('comic/nuevo', CrearComic.as_view(), name='Comic_New'),
    path('comic/<pk>', ComicDetalle. as_view(), name= 'Comic_Detail'),
    
    path('musica/list', MusicaList.as_view(), name= 'musica_List'),
    path('musica/nuevo', CrearMusica.as_view(), name='musica_New'),
    path('musica/<pk>', MusicaDetalle. as_view(), name= 'musica_Detail'),

]