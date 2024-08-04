from django.urls import path
from appisn.views import *

urlpatterns = [
    path ('',inicio, name="inicio"),
    path('cursos', cursos, name="cursos"),
    path('estudiantes',estudiantes, name= "estudiantes"),
    path('profesores', profesores, name= "profesores"),
    path('entregables', entregables, name= "entregables"),
    path('cursoFormulario', cursoFormulario, name= "Cursoformulario"),
    #path('form-con-api',form_con_api, name="Form-Con-Api"),#
    path('profesorFormulario', profesorFormulario, name="ProfesorFormulario"),
    path('login', login_request, name="Login"),
    path('register', register, name="Register"),
    #path('logout', LogoutView.as_view(template_name='appisn/logout.html'), name = 'Logout'),
]