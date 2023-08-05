from django.shortcuts import render
from Registro.forms import UserRegisterForm


def register(request):

      if request.method == 'POST':

            
            form = UserRegisterForm(request.POST)
            if form.is_valid():

                  username = form.cleaned_data['username']
                  form.save()
                  return render(request,"LogApp/login.html" ,  {"mensaje":"Usuario Creado :)"})

      else:
                 
            form = UserRegisterForm()     

      return render(request,"Registro/registro.html" ,  {"form":form})