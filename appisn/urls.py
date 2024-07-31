from django.urls import path
from appisn.views import *

urlpatterns = [
    path ('',inicio, name="inicio"),
    path('cursos', cursos, name="cursos"),
    path('estudiantes',estudiantes, name= "estudiantes"),
    path('profesores', profesores, name= "profesores"),
    path('entregables', entregables, name= "entregables"),
    path('cursoFormulario', cursoFormulario, name= "cursoformulario"),
    #path('form-con-api',form_con_api, name="Form-Con-Api"),#
    path('profesorFormulario', profesorFormulario, name="ProfesorFormulario"),
    
]