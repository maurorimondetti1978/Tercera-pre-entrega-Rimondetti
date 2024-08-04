from django.shortcuts import render
from appisn.models import Curso
from appisn.forms import CursoFormulario
from appisn.models import Profesor
from appisn.forms import ProfesorFormulario
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.views import LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# Create your views here.   
def inicio(request):
    return render(request, "appisn/inicio.html")

def cursos(request):
    cursos = Curso.objects.all()
    return render(request, "appisn/cursos.html", {"cursos": cursos})


def estudiantes(request):
    return render(request, "appisn/estudiantes.html")

def profesores(request):
    profesores = Profesor.objects.all()
    return render(request, "appisn/profesores.html")

def entregables(request):
    return render(request, "appisn/entregables.html")

def cursoFormulario(request):
    if request.method == 'POST':
 
        curso = Curso(request.post['curso'],(request.post['camada']))

        curso.save()

        return render(request, "appisn/inicio.html")
    
    return render(request,"appisn/cursoFormulario.html")


def cursoFormulario(request):

    if request.method == 'POST':

        miFormulario= CursoFormulario(request.POST)
        
        print(miFormulario)

        if miFormulario.is_valid:

            informacion= miFormulario.cleaned_data

            curso =  Curso(nombre=informacion['curso'], camada=informacion['camada'])

            curso.save()

            return render(request, "appisn/inicio.html")

   
    else:
        mi_formulario = CursoFormulario()

    return render(request, "appisn/cursoFormulario.html", {"mi_formulario": mi_formulario})

def profesorFormulario(request):

    if request.method == 'POST':

        miFormulario= ProfesorFormulario(request.POST)
        
        print(miFormulario)

        if miFormulario.is_valid:

            informacion= miFormulario.cleaned_data

            profesor = Profesor (nombre=informacion['nombre'], apellido=informacion['apellido'], email=informacion['email'], profesion=informacion['profesion'])


            profesor.save()

            return render(request, "appisn/inicio.html")

   
    else:
        mi_formulario = ProfesorFormulario()

    return render(request, "appisn/profesorFormulario.html", {"mi_formulario": mi_formulario})

def login_request(request):

    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contra = form.cleaned_data.get('password')

            user = authenticate(username=usuario, password=contra)

            if user is not None:
                login(request, user)

                return render(request, "appisn/inicio.html", {"mensaje":f"Bienvenido {usuario}"})
            else:

                return render(request, "appisn/inicio.html", {"mensaje":"Error, datos incorrectos"})
        
        else:

                return render(request,"appisn/inicio.html" , {"mensaje": "Error, formulario erroneo"})

    form = AuthenticationForm()

    return render(request, "appisn/login.html", {'form':form})

def register(request):

    if request.method == 'POST':

        form = UserCreationForm(request.POST)

        if form.is_valid():

            username= form.cleaned_data['username']
            form.save()
            return render(request, "appisn/inicio.html", {"mensaje": "Usuario Creado:)"})
        
    else:
        form= UserCreationForm()

    return render(request, "appisn/registro.html" , {"form": form})

"""def register(request):

    if request.method == 'POST':

        form = UserRegisterForm(request.POST)

        if form.is_valid():

            username= form.cleaned_data['username']
            form.save()
            return render(request, "appisn/inicio.html", {"mensaje": "Usuario Creado:)"})
        
    else:
        form= UserRegisterForm()

    return render(request, "appisn/registro.html" , {"form": form})"""

@login_required
def inicio(request):
    return render(request, "appisn/inicio.html")

            
            

    



