from django.shortcuts import render
from Profile.forms import AvatarFormulario,UserEditForm
from Registro.forms import User

def agregarAvatar(request):
    if request.method == "POST":
        miFormulario = AvatarFormulario(request.POST, request.FILES)
        if miFormulario.is_valid():
            u = User.objects.get(username=request.user)
            #avatar = Avatar(user=u, imagen=miFormulario.cleaned_data['imagen'])
            #avatar.save()

            return render(request, "AppCoder/inicio.html")
    else:
        miFormulario=AvatarFormulario()
        
    return render(request, "AppCoder/agregarAvatar.html", {'miFormulario': miFormulario})
    


#@login_required
def editarPerfil(request):

    usuario = request.user

    if request.method == 'POST':

        miFormulario = UserEditForm(request.POST)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            usuario.email = informacion['email']
            usuario.password1 = informacion['password1']
            usuario.password2 = informacion['password2']
            usuario.last_name = informacion['last_name']
            usuario.first_name = informacion['first_name']

            usuario.save()

            return render(request, "AppCoder/inicio.html")

    else:

        miFormulario = UserEditForm(initial={'email': usuario.email})

    return render(request, "AppCoder/editarPerfil.html", {"miFormulario": miFormulario, "usuario": usuario})
