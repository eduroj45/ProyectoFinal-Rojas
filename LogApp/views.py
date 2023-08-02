from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,authenticate


def login_request(request):

    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():  

            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')

            user = authenticate(username= usuario, password=contrasenia)

            if user is not None:
                login(request, user)

                return render(request, "principal/inicio.html", {"mensaje":f"Bienvenido {usuario}"})
            else:
                return render(request, "principal/inicio.html", {"mensaje":"Datos incorrectos"})
           
        else:

            return render(request, "principal/inicio.html", {"mensaje":"Formulario erroneo"})

    form = AuthenticationForm()

    return render(request, "LogApp/login.html", {"form": form})