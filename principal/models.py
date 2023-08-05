from django.db import models
from django.contrib.auth.models import User




class Avatar(models.Model):
   
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    imagen = models.ImageField(upload_to='avatares', null=True, blank = True)
 
    def __str__(self):
        return f"{self.user} - {self.imagen}"
    
class Pelicula(models.Model):
    nombre= models.CharField(max_length=50)
    precio= models.IntegerField()
    imagen= models.ImageField(upload_to='media', null=True , blank =True)
    estado= models.CharField(max_length=20)
    genero= models.CharField(max_length= 30)
    descripcion= models.CharField(max_length= 500)
    fecha=models.DateTimeField(auto_now=False)
    vendedor= models.CharField(max_length= 50)
    contacto= models.CharField(max_length=100)
    
class Comic(models.Model):
    nombre= models.CharField(max_length=30)
    precio= models.IntegerField()
    imagen= models.ImageField(upload_to='media', null=True , blank =True)
    estado= models.CharField(max_length=20)
    editorial= models.CharField(max_length=20)
    descripcion= models.CharField(max_length= 500)
    fecha=models.DateTimeField(auto_now=False)


    vendedor= models.CharField(max_length= 50)
    contacto= models.CharField(max_length=100)
    
class Musica(models.Model):
    artista= models.CharField(max_length=50)
    precio= models.IntegerField()
    imagen= models.ImageField(upload_to='media', null=True , blank =True)
    disco= models.CharField(max_length=50)
    genero= models.CharField(max_length=30)
    estado= models.CharField(max_length=20)
    descripcion= models.CharField(max_length= 500)
    fecha=models.DateTimeField(auto_now=False)
    vendedor= models.CharField(max_length= 50)
    contacto= models.CharField(max_length=100)
    
       
        
        
        
        
    
    
