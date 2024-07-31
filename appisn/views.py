from django.shortcuts import render
from appisn.models import Curso
from appisn.forms import CursoFormulario
from appisn.models import Profesor
from appisn.forms import ProfesorFormulario


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


